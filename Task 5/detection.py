from database import get_connection
from datetime import datetime, timezone


# ============================================================
# DETECTION CONFIGURATION
# ============================================================

SSH_FAILURE_THRESHOLD = 5
SSH_TIME_WINDOW_SECONDS = 60

PORT_SCAN_THRESHOLD = 5

AUTH_FAILURE_THRESHOLD = 3
AUTH_FAILURE_WINDOW_SECONDS = 60


# ============================================================
# CREATE INCIDENT FOR HIGH / CRITICAL ALERT
# ============================================================

def create_incident_for_alert(connection, alert_id):

    existing_incident = connection.execute("""
        SELECT id
        FROM incidents
        WHERE alert_id = ?
    """, (alert_id,)).fetchone()

    if existing_incident:
        return None

    alert = connection.execute("""
        SELECT *
        FROM alerts
        WHERE id = ?
    """, (alert_id,)).fetchone()

    if not alert:
        return None

    if alert["severity"] not in ("HIGH", "CRITICAL"):
        return None

    title = f"{alert['alert_type']} Incident"

    connection.execute("""
        INSERT INTO incidents
        (
            alert_id,
            title,
            severity,
            source_ip,
            destination_ip,
            description,
            status,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        alert["id"],
        title,
        alert["severity"],
        alert["source_ip"],
        alert["destination_ip"],
        alert["description"],
        "OPEN",
        datetime.now(timezone.utc).isoformat()
    ))

    return connection.execute(
        "SELECT last_insert_rowid()"
    ).fetchone()[0]


# ============================================================
# SSH BRUTE FORCE DETECTION
#
# Rule:
# 5 or more failed SSH authentication attempts
# from the same source against the same destination
# within 60 seconds.
# ============================================================

def detect_ssh_brute_force(connection):

    rows = connection.execute("""
        SELECT
            source_ip,
            destination_ip,
            timestamp
        FROM events
        WHERE event_type = 'SSH_AUTH_FAILURE'
        ORDER BY timestamp ASC
    """).fetchall()

    alerts_created = 0

    grouped_events = {}

    for row in rows:

        key = (
            row["source_ip"],
            row["destination_ip"]
        )

        if key not in grouped_events:
            grouped_events[key] = []

        grouped_events[key].append(row)

    for key, events in grouped_events.items():

        source_ip = key[0]
        destination_ip = key[1]

        if len(events) < SSH_FAILURE_THRESHOLD:
            continue

        previous_alert = connection.execute("""
            SELECT id, timestamp
            FROM alerts
            WHERE alert_type = 'SSH_BRUTE_FORCE'
              AND source_ip = ?
              AND destination_ip = ?
            ORDER BY id DESC
            LIMIT 1
        """, (
            source_ip,
            destination_ip
        )).fetchone()

        resolved_time = None

        if previous_alert:

            previous_incident = connection.execute("""
                SELECT resolved_at
                FROM incidents
                WHERE alert_id = ?
                ORDER BY id DESC
                LIMIT 1
            """, (
                previous_alert["id"],
            )).fetchone()

            if previous_incident:

                if previous_incident["resolved_at"]:

                    resolved_time = datetime.fromisoformat(
                        previous_incident["resolved_at"]
                    )

        if resolved_time:

            new_events = []

            for event in events:

                event_time = datetime.fromisoformat(
                    event["timestamp"]
                )

                if event_time > resolved_time:
                    new_events.append(event)

            events = new_events

        if len(events) < SSH_FAILURE_THRESHOLD:
            continue

        existing_open_alert = connection.execute("""
            SELECT id
            FROM alerts
            WHERE alert_type = 'SSH_BRUTE_FORCE'
              AND source_ip = ?
              AND destination_ip = ?
              AND status = 'OPEN'
        """, (
            source_ip,
            destination_ip
        )).fetchone()

        if existing_open_alert:
            continue

        detection_window = None

        for i in range(len(events)):

            first_time = datetime.fromisoformat(
                events[i]["timestamp"]
            )

            window_events = []

            for j in range(i, len(events)):

                current_time = datetime.fromisoformat(
                    events[j]["timestamp"]
                )

                elapsed = (
                    current_time - first_time
                ).total_seconds()

                if elapsed <= SSH_TIME_WINDOW_SECONDS:

                    window_events.append(
                        events[j]
                    )

                else:

                    break

            if len(window_events) >= SSH_FAILURE_THRESHOLD:

                detection_window = window_events

                break

        if not detection_window:
            continue

        first_attack_time = datetime.fromisoformat(
            detection_window[0]["timestamp"]
        )

        last_attack_time = datetime.fromisoformat(
            detection_window[-1]["timestamp"]
        )

        attack_duration = int(
            (
                last_attack_time
                - first_attack_time
            ).total_seconds()
        )

        failure_count = len(
            detection_window
        )

        description = (
            f"Possible SSH brute-force attack detected. "
            f"{failure_count} failed authentication attempts "
            f"from {source_ip} against {destination_ip} "
            f"within {attack_duration} seconds. "
            f"Detection rule: {SSH_FAILURE_THRESHOLD} "
            f"failures within "
            f"{SSH_TIME_WINDOW_SECONDS} seconds."
        )

        cursor = connection.execute("""
            INSERT INTO alerts
            (
                timestamp,
                alert_type,
                source_ip,
                destination_ip,
                severity,
                description,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            datetime.now(timezone.utc).isoformat(),
            "SSH_BRUTE_FORCE",
            source_ip,
            destination_ip,
            "HIGH",
            description,
            "OPEN"
        ))

        alert_id = cursor.lastrowid

        create_incident_for_alert(
            connection,
            alert_id
        )

        alerts_created += 1

    return alerts_created


# ============================================================
# PORT SCAN DETECTION
#
# Rule:
# 5 or more different destination ports
# from the same source against the same destination.
# ============================================================

def detect_port_scan(connection):

    rows = connection.execute("""
        SELECT
            source_ip,
            destination_ip,
            COUNT(DISTINCT destination_port) AS port_count
        FROM events
        WHERE event_type = 'PORT_SCAN'
          AND destination_port IS NOT NULL
        GROUP BY source_ip, destination_ip
        HAVING COUNT(DISTINCT destination_port) >= ?
    """, (PORT_SCAN_THRESHOLD,)).fetchall()

    alerts_created = 0

    for row in rows:

        existing_alert = connection.execute("""
            SELECT id
            FROM alerts
            WHERE alert_type = 'PORT_SCAN'
              AND source_ip = ?
              AND destination_ip = ?
              AND status = 'OPEN'
        """, (
            row["source_ip"],
            row["destination_ip"]
        )).fetchone()

        if existing_alert:
            continue

        description = (
            f"Possible port scan detected. "
            f"Source {row['source_ip']} "
            f"attempted connections to "
            f"{row['port_count']} different ports "
            f"on {row['destination_ip']}."
        )

        cursor = connection.execute("""
            INSERT INTO alerts
            (
                timestamp,
                alert_type,
                source_ip,
                destination_ip,
                severity,
                description,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            datetime.now(timezone.utc).isoformat(),
            "PORT_SCAN",
            row["source_ip"],
            row["destination_ip"],
            "MEDIUM",
            description,
            "OPEN"
        ))

        alert_id = cursor.lastrowid

        create_incident_for_alert(
            connection,
            alert_id
        )

        alerts_created += 1

    return alerts_created


# ============================================================
# REPEATED AUTHENTICATION FAILURE DETECTION
#
# Rule:
# 3 or more failed authentication attempts
# against the same username within 60 seconds.
# ============================================================

def detect_repeated_auth_failures(connection):

    rows = connection.execute("""
        SELECT
            source_ip,
            destination_ip,
            username,
            timestamp
        FROM events
        WHERE event_type = 'SSH_AUTH_FAILURE'
          AND username IS NOT NULL
          AND username != 'unknown'
        ORDER BY timestamp ASC
    """).fetchall()

    alerts_created = 0

    grouped_events = {}

    for row in rows:

        key = (
            row["source_ip"],
            row["destination_ip"],
            row["username"]
        )

        if key not in grouped_events:
            grouped_events[key] = []

        grouped_events[key].append(row)

    for key, events in grouped_events.items():

        source_ip = key[0]
        destination_ip = key[1]
        username = key[2]

        if len(events) < AUTH_FAILURE_THRESHOLD:
            continue

        existing_open_alert = connection.execute("""
            SELECT id
            FROM alerts
            WHERE alert_type = 'REPEATED_AUTH_FAILURE'
              AND source_ip = ?
              AND destination_ip = ?
              AND status = 'OPEN'
        """, (
            source_ip,
            destination_ip
        )).fetchone()

        if existing_open_alert:
            continue

        detection_window = None

        for i in range(len(events)):

            first_time = datetime.fromisoformat(
                events[i]["timestamp"]
            )

            window_events = []

            for j in range(i, len(events)):

                current_time = datetime.fromisoformat(
                    events[j]["timestamp"]
                )

                elapsed = (
                    current_time - first_time
                ).total_seconds()

                if elapsed <= AUTH_FAILURE_WINDOW_SECONDS:

                    window_events.append(
                        events[j]
                    )

                else:

                    break

            if len(window_events) >= AUTH_FAILURE_THRESHOLD:

                detection_window = window_events

                break

        if not detection_window:
            continue

        first_time = datetime.fromisoformat(
            detection_window[0]["timestamp"]
        )

        last_time = datetime.fromisoformat(
            detection_window[-1]["timestamp"]
        )

        duration = int(
            (
                last_time - first_time
            ).total_seconds()
        )

        failure_count = len(
            detection_window
        )

        description = (
            f"Repeated authentication failures detected. "
            f"{failure_count} failed login attempts for "
            f"user '{username}' from {source_ip} "
            f"against {destination_ip} within "
            f"{duration} seconds. "
            f"Detection rule: "
            f"{AUTH_FAILURE_THRESHOLD} failures within "
            f"{AUTH_FAILURE_WINDOW_SECONDS} seconds."
        )

        connection.execute("""
            INSERT INTO alerts
            (
                timestamp,
                alert_type,
                source_ip,
                destination_ip,
                severity,
                description,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            datetime.now(timezone.utc).isoformat(),
            "REPEATED_AUTH_FAILURE",
            source_ip,
            destination_ip,
            "MEDIUM",
            description,
            "OPEN"
        ))

        alerts_created += 1

    return alerts_created


# ============================================================
# RUN ALL DETECTIONS
# ============================================================

def run_all_detections():

    connection = get_connection()

    try:

        ssh_alerts = detect_ssh_brute_force(
            connection
        )

        port_scan_alerts = detect_port_scan(
            connection
        )

        auth_failure_alerts = (
            detect_repeated_auth_failures(
                connection
            )
        )

        connection.commit()

        return {
            "ssh_brute_force_alerts": ssh_alerts,
            "port_scan_alerts": port_scan_alerts,
            "repeated_auth_failure_alerts":
                auth_failure_alerts,
            "total_alerts":
                ssh_alerts
                + port_scan_alerts
                + auth_failure_alerts
        }

    finally:

        connection.close()


# ============================================================
# COMMAND-LINE TEST
# ============================================================

if __name__ == "__main__":

    results = run_all_detections()

    print(
        "Detection completed."
    )

    print(
        f"SSH brute-force alerts: "
        f"{results['ssh_brute_force_alerts']}"
    )

    print(
        f"Port-scan alerts: "
        f"{results['port_scan_alerts']}"
    )

    print(
        f"Repeated authentication alerts: "
        f"{results['repeated_auth_failure_alerts']}"
    )

    print(
        f"Total new alerts: "
        f"{results['total_alerts']}"
    )
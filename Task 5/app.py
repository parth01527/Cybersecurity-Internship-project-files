from flask import Flask, request, jsonify, render_template
from database import get_connection, initialize_database
from detection import run_all_detections
from datetime import datetime, timezone

app = Flask(__name__)

initialize_database()


def utc_now():
    return datetime.now(timezone.utc).isoformat()


# ============================================================
# DASHBOARD
# ============================================================

@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ============================================================
# CREATE EVENT
# ============================================================

@app.route("/api/events", methods=["POST"])
def create_event():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "JSON body required"
        }), 400

    event_type = data.get("event_type")

    if not event_type:
        return jsonify({
            "error": "event_type is required"
        }), 400

    timestamp = data.get(
        "timestamp",
        utc_now()
    )

    source_ip = data.get("source_ip")
    destination_ip = data.get("destination_ip")
    destination_port = data.get("destination_port")
    username = data.get("username")
    message = data.get("message")
    severity = data.get("severity", "LOW")

    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO events (
            timestamp,
            event_type,
            source_ip,
            destination_ip,
            destination_port,
            username,
            message,
            severity
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            timestamp,
            event_type,
            source_ip,
            destination_ip,
            destination_port,
            username,
            message,
            severity
        )
    )

    event_id = cursor.lastrowid

    connection.commit()
    connection.close()

    try:

        detection_result = run_all_detections()

        print(
            "AUTOMATIC DETECTION RESULT:",
            detection_result
        )

    except Exception as error:

        print(
            "Detection error:",
            error
        )

        detection_result = {
            "error": str(error)
        }

    return jsonify({
        "message": "Event received successfully",
        "event_id": event_id,
        "detection": detection_result
    }), 201


# ============================================================
# GET EVENTS
# ============================================================

@app.route("/api/events", methods=["GET"])
def get_events():

    connection = get_connection()

    rows = connection.execute(
        """
        SELECT *
        FROM events
        ORDER BY id DESC
        """
    ).fetchall()

    connection.close()

    return jsonify([
        dict(row)
        for row in rows
    ])


# ============================================================
# GET ALERTS
# ============================================================

@app.route("/api/alerts", methods=["GET"])
def get_alerts():

    connection = get_connection()

    rows = connection.execute(
        """
        SELECT *
        FROM alerts
        ORDER BY id DESC
        """
    ).fetchall()

    connection.close()

    return jsonify([
        dict(row)
        for row in rows
    ])


# ============================================================
# UPDATE ALERT STATUS
# ============================================================

@app.route(
    "/api/alerts/<int:alert_id>/status",
    methods=["PUT"]
)
def update_alert_status(alert_id):

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "JSON body required"
        }), 400

    new_status = data.get("status")

    allowed_statuses = [
        "OPEN",
        "RESOLVED"
    ]

    if new_status not in allowed_statuses:
        return jsonify({
            "error": "Invalid status"
        }), 400

    connection = get_connection()

    alert = connection.execute(
        """
        SELECT *
        FROM alerts
        WHERE id = ?
        """,
        (alert_id,)
    ).fetchone()

    if not alert:

        connection.close()

        return jsonify({
            "error": "Alert not found"
        }), 404

    connection.execute(
        """
        UPDATE alerts
        SET status = ?
        WHERE id = ?
        """,
        (
            new_status,
            alert_id
        )
    )

    connection.commit()
    connection.close()

    return jsonify({
        "message": "Alert status updated successfully",
        "alert_id": alert_id,
        "status": new_status
    })


# ============================================================
# GET INCIDENTS
# ============================================================

@app.route("/api/incidents", methods=["GET"])
def get_incidents():

    connection = get_connection()

    rows = connection.execute(
        """
        SELECT *
        FROM incidents
        ORDER BY id DESC
        """
    ).fetchall()

    connection.close()

    return jsonify([
        dict(row)
        for row in rows
    ])


# ============================================================
# INVESTIGATE INCIDENT
# ============================================================

@app.route(
    "/api/incidents/<int:incident_id>",
    methods=["GET"]
)
def investigate_incident(incident_id):

    connection = get_connection()

    incident = connection.execute(
        """
        SELECT *
        FROM incidents
        WHERE id = ?
        """,
        (incident_id,)
    ).fetchone()

    if not incident:

        connection.close()

        return jsonify({
            "error": "Incident not found"
        }), 404

    incident = dict(incident)

    source_ip = incident["source_ip"]
    destination_ip = incident["destination_ip"]
    created_at = incident["created_at"]

    previous_incident = connection.execute(
        """
        SELECT *
        FROM incidents
        WHERE source_ip = ?
          AND destination_ip = ?
          AND status = 'RESOLVED'
          AND id < ?
        ORDER BY id DESC
        LIMIT 1
        """,
        (
            source_ip,
            destination_ip,
            incident_id
        )
    ).fetchone()

    if previous_incident:

        previous_resolved_at = (
            previous_incident["resolved_at"]
        )

        events = connection.execute(
            """
            SELECT *
            FROM events
            WHERE event_type = 'SSH_AUTH_FAILURE'
              AND source_ip = ?
              AND destination_ip = ?
              AND timestamp > ?
              AND timestamp <= ?
            ORDER BY timestamp ASC
            """,
            (
                source_ip,
                destination_ip,
                previous_resolved_at,
                created_at
            )
        ).fetchall()

    else:

        events = connection.execute(
            """
            SELECT *
            FROM events
            WHERE event_type = 'SSH_AUTH_FAILURE'
              AND source_ip = ?
              AND destination_ip = ?
              AND timestamp <= ?
            ORDER BY timestamp DESC
            LIMIT 20
            """,
            (
                source_ip,
                destination_ip,
                created_at
            )
        ).fetchall()

        events = list(reversed(events))

    events = [
        dict(event)
        for event in events
    ]

    failed_attempt_count = len(events)

    first_observed = None
    last_observed = None
    attack_duration_seconds = 0

    if events:

        first_observed = events[0]["timestamp"]
        last_observed = events[-1]["timestamp"]

        try:

            first_time = datetime.fromisoformat(
                first_observed.replace(
                    "Z",
                    "+00:00"
                )
            )

            last_time = datetime.fromisoformat(
                last_observed.replace(
                    "Z",
                    "+00:00"
                )
            )

            attack_duration_seconds = (
                last_time - first_time
            ).total_seconds()

        except Exception:

            attack_duration_seconds = 0

    attack_statistics = {
        "failed_attempt_count": failed_attempt_count,
        "threshold": 5,
        "first_observed": first_observed,
        "last_observed": last_observed,
        "attack_duration_seconds": attack_duration_seconds
    }

    connection.close()

    return jsonify({
        "incident": incident,
        "events": events,
        "attack_statistics": attack_statistics
    })


# ============================================================
# UPDATE INCIDENT STATUS
# ============================================================

@app.route(
    "/api/incidents/<int:incident_id>/status",
    methods=["PUT"]
)
def update_incident_status(incident_id):

    data = request.get_json()

    if not data:

        return jsonify({
            "error": "JSON body required"
        }), 400

    new_status = data.get("status")

    allowed_statuses = [
        "OPEN",
        "INVESTIGATING",
        "RESOLVED"
    ]

    if new_status not in allowed_statuses:

        return jsonify({
            "error": "Invalid status"
        }), 400

    connection = get_connection()

    incident = connection.execute(
        """
        SELECT *
        FROM incidents
        WHERE id = ?
        """,
        (incident_id,)
    ).fetchone()

    if not incident:

        connection.close()

        return jsonify({
            "error": "Incident not found"
        }), 404

    if new_status == "RESOLVED":

        resolved_at = utc_now()

        connection.execute(
            """
            UPDATE incidents
            SET status = ?,
                resolved_at = ?
            WHERE id = ?
            """,
            (
                new_status,
                resolved_at,
                incident_id
            )
        )

        connection.execute(
            """
            UPDATE alerts
            SET status = 'RESOLVED'
            WHERE id = ?
            """,
            (incident["alert_id"],)
        )

    else:

        connection.execute(
            """
            UPDATE incidents
            SET status = ?,
                resolved_at = NULL
            WHERE id = ?
            """,
            (
                new_status,
                incident_id
            )
        )

        connection.execute(
            """
            UPDATE alerts
            SET status = ?
            WHERE id = ?
            """,
            (
                new_status,
                incident["alert_id"]
            )
        )

    connection.commit()
    connection.close()

    return jsonify({
        "message": "Incident status updated successfully",
        "incident_id": incident_id,
        "status": new_status
    })


# ============================================================
# START MINI-SIEM
# ============================================================

if __name__ == "__main__":

    print()
    print("==========================================")
    print("        MINI-SIEM SECURITY PLATFORM")
    print("==========================================")
    print()
    print("SIEM Server:")
    print("http://192.168.56.1:5000")
    print()
    print("Database:")
    print(r"C:\MiniSIEM\siem.db")
    print()
    print("Debug mode: OFF")
    print("Automatic detection: ON")
    print("Detection diagnostics: ON")
    print("==========================================")
    print()

    app.run(
        host="192.168.56.1",
        port=5000,
        debug=False,
        use_reloader=False
    )
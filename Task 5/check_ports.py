import sqlite3

connection = sqlite3.connect("siem.db")

rows = connection.execute("""
    SELECT
        source_ip,
        destination_ip,
        COUNT(DISTINCT destination_port) AS port_count
    FROM events
    WHERE event_type = 'PORT_SCAN'
    GROUP BY source_ip, destination_ip
""").fetchall()

print(rows)

connection.close()
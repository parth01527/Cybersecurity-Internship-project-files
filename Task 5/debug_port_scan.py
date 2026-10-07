import sqlite3

connection = sqlite3.connect("siem.db")
connection.row_factory = sqlite3.Row

rows = connection.execute("""
    SELECT
        source_ip,
        destination_ip,
        COUNT(DISTINCT destination_port) AS port_count
    FROM events
    WHERE event_type = 'PORT_SCAN'
      AND destination_port IS NOT NULL
    GROUP BY source_ip, destination_ip
    HAVING COUNT(DISTINCT destination_port) >= 5
""").fetchall()

print("Detection query result:")

for row in rows:
    print(dict(row))

connection.close()

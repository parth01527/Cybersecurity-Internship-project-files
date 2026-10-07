import sqlite3

connection = sqlite3.connect("siem.db")
connection.row_factory = sqlite3.Row

rows = connection.execute("""
    SELECT
        id,
        timestamp
    FROM events
    WHERE event_type = 'SSH_AUTH_FAILURE'
    ORDER BY id DESC
    LIMIT 10
""").fetchall()

for row in reversed(rows):
    print(dict(row))

connection.close()
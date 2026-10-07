import sqlite3
import os


# ============================================================
# DATABASE LOCATION
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATABASE = os.path.join(
    BASE_DIR,
    "siem.db"
)


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():

    connection = sqlite3.connect(
        DATABASE
    )

    connection.row_factory = sqlite3.Row

    return connection


# ============================================================
# INITIALIZE DATABASE
# ============================================================

def initialize_database():

    connection = get_connection()


    # --------------------------------------------------------
    # SECURITY EVENTS
    # --------------------------------------------------------

    connection.execute("""
        CREATE TABLE IF NOT EXISTS events (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT NOT NULL,

            event_type TEXT NOT NULL,

            source_ip TEXT,

            destination_ip TEXT,

            destination_port INTEGER,

            username TEXT,

            message TEXT,

            severity TEXT DEFAULT 'LOW'
        )
    """)


    # --------------------------------------------------------
    # SECURITY ALERTS
    # --------------------------------------------------------

    connection.execute("""
        CREATE TABLE IF NOT EXISTS alerts (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT NOT NULL,

            alert_type TEXT NOT NULL,

            source_ip TEXT,

            destination_ip TEXT,

            severity TEXT NOT NULL,

            description TEXT NOT NULL,

            status TEXT DEFAULT 'OPEN'
        )
    """)


    # --------------------------------------------------------
    # SECURITY INCIDENTS
    # --------------------------------------------------------

    connection.execute("""
        CREATE TABLE IF NOT EXISTS incidents (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            alert_id INTEGER NOT NULL,

            title TEXT NOT NULL,

            severity TEXT NOT NULL,

            source_ip TEXT,

            destination_ip TEXT,

            description TEXT NOT NULL,

            status TEXT DEFAULT 'OPEN',

            created_at TEXT NOT NULL,

            resolved_at TEXT,

            FOREIGN KEY (alert_id)
                REFERENCES alerts(id)
        )
    """)


    connection.commit()

    connection.close()


# ============================================================
# COMMAND-LINE INITIALIZATION
# ============================================================

if __name__ == "__main__":

    initialize_database()

    print(
        "SIEM database initialized successfully."
    )

    print(
        "Database location:"
    )

    print(
        DATABASE
    )
import sqlite3
import os

DB_PATH = os.path.join("data", "vehicle.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS telemetry (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vehicle_id TEXT,
        timestamp TEXT,
        speed REAL,
        rpm INTEGER,
        engine_temp REAL,
        fuel_level REAL,
        vibration REAL
    )
    """)

    conn.commit()
    conn.close()


def insert_telemetry(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO telemetry (
        vehicle_id,
        timestamp,
        speed,
        rpm,
        engine_temp,
        fuel_level,
        vibration
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data["vehicle_id"],
        data["timestamp"],
        data["speed"],
        data["rpm"],
        data["engine_temp"],
        data["fuel_level"],
        data["vibration"]
    ))

    conn.commit()
    conn.close()
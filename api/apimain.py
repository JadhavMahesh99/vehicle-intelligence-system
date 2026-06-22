from fastapi import FastAPI
import sqlite3

app = FastAPI(
    title="Vehicle Intelligence API"
)


@app.get("/")
def home():
    return {
        "message": "Vehicle Intelligence System Running"
    }


@app.get("/vehicles")
def get_vehicles():

    conn = sqlite3.connect("data/vehicle.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM telemetry
    ORDER BY id DESC
    LIMIT 20
    """)

    rows = cursor.fetchall()

    conn.close()

    return {
        "records": rows
    }
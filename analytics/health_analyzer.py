import sqlite3


def calculate_health_score(speed, engine_temp, vibration):

    score = 100

    if engine_temp > 100:
        score -= 30

    if vibration > 6:
        score -= 25

    if speed > 120:
        score -= 15

    return max(score, 0)


def analyze_latest_data():

    conn = sqlite3.connect("data/vehicle.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT vehicle_id,
               speed,
               engine_temp,
               vibration
        FROM telemetry
        ORDER BY id DESC
        LIMIT 10
    """)

    rows = cursor.fetchall()

    print("\n🚗 VEHICLE HEALTH REPORT\n")

    for row in rows:

        vehicle_id = row[0]
        speed = row[1]
        temp = row[2]
        vibration = row[3]

        score = calculate_health_score(
            speed,
            temp,
            vibration
        )

        print(f"Vehicle : {vehicle_id}")
        print(f"Health Score : {score}/100")

        if score < 60:
            print("⚠ Maintenance Required")

        print("-" * 40)

    conn.close()


if __name__ == "__main__":
    analyze_latest_data()
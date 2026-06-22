import sqlite3
import pandas as pd
from sklearn.ensemble import IsolationForest

conn = sqlite3.connect("data/vehicle.db")

df = pd.read_sql_query("""
SELECT speed,
       rpm,
       engine_temp,
       fuel_level,
       vibration
FROM telemetry
""", conn)

conn.close()

print(f"Records Loaded: {len(df)}")

if len(df) < 20:
    print("Run simulator longer to generate more data.")
    exit()

model = IsolationForest(
    contamination=0.05,
    random_state=42
)

df["anomaly"] = model.fit_predict(df)

anomalies = df[df["anomaly"] == -1]

print("\n🚨 ANOMALY DETECTION REPORT\n")

if len(anomalies) == 0:
    print("No anomalies detected.")
else:
    print(anomalies.head(20))
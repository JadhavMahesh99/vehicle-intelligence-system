import streamlit as st
import sqlite3
import pandas as pd
import time
from sklearn.ensemble import IsolationForest

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Vehicle Performance Analytics System",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("🚗 Vehicle Performance Analytics System (LIVE)")

# -----------------------------
# LOAD DATA
# -----------------------------
conn = sqlite3.connect("data/vehicle.db")

df = pd.read_sql_query(
    "SELECT * FROM telemetry ORDER BY id DESC LIMIT 100",
    conn
)

conn.close()

# -----------------------------
# SAFETY CHECK
# -----------------------------
if df.empty:
    st.warning("No data found in database")
    st.stop()

# -----------------------------
# ML ANOMALY DETECTION
# -----------------------------
features = df[["speed", "engine_temp", "fuel_level"]]

model = IsolationForest(contamination=0.1, random_state=42)

df["anomaly"] = model.fit_predict(features)

# -----------------------------
# HEALTH SCORE FUNCTION
# -----------------------------
def calculate_health_score(df):
    score = 100

    if df["engine_temp"].mean() > 90:
        score -= 25

    if df["fuel_level"].diff().mean() < -0.5:
        score -= 25

    if df["speed"].std() > 30:
        score -= 15

    return max(score, 0)

score = calculate_health_score(df)

# -----------------------------
# METRICS
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("🚗 Health Score", f"{score}/100")
col2.metric("⛽ Fuel Level", f"{df['fuel_level'].iloc[-1]}%")
col3.metric("🌡 Engine Temp", f"{df['engine_temp'].iloc[-1]}°C")

# -----------------------------
# CHARTS
# -----------------------------
st.subheader("📊 Vehicle Trends")

st.line_chart(
    df.set_index("timestamp")[["speed", "engine_temp", "fuel_level"]]
)

# -----------------------------
# ALERTS
# -----------------------------
st.subheader("🚨 System Alerts")

latest = df.iloc[-1]

alerts = []

if latest["engine_temp"] > 95:
    alerts.append("⚠ Engine Overheating")

if latest["fuel_level"] < 15:
    alerts.append("⛽ Low Fuel Warning")

if latest["speed"] > 120:
    alerts.append("🚨 Overspeed Detected")

if latest["anomaly"] == -1:
    alerts.append("🧠 ML Anomaly Detected")

if len(alerts) == 0:
    st.success("All systems normal ✅")
else:
    for a in alerts:
        st.error(a)

# -----------------------------
# ANOMALY TABLE
# -----------------------------
st.subheader("🧠 Detected Anomalies")

st.dataframe(df[df["anomaly"] == -1])

# -----------------------------
# AUTO REFRESH (LIVE SYSTEM)
# -----------------------------
time.sleep(3)
st.rerun()
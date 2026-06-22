🚗 Vehicle Intelligence System
📌 Overview

The Vehicle Intelligence System is a full-stack AI-powered automotive analytics platform that simulates, collects, processes, and analyzes vehicle telemetry data. It provides real-time monitoring, anomaly detection using Machine Learning, and an interactive dashboard for insights.

⚙️ Features
🚗 Real-time vehicle telemetry simulation
📊 Live dashboard using Streamlit
🧠 ML-based anomaly detection (Isolation Forest)
📈 Vehicle health score calculation
🚨 Smart alert system (overheat, low fuel, overspeed)
🗄️ SQLite database integration
⚡ Modular architecture (API, ML, Analytics, Dashboard)

🏗️ System Architecture
Simulator → Data → Database → API → ML → Analytics → Dashboard

📁 Project Structure
vehicle-intelligence-system/
│
├── analytics/        # Health scoring & analysis logic
│   ├── health_analyzer.py
│   ├── healthscore.py
│
├── api/              # Backend API layer
│   ├── main.py
│   ├── apimain.py
│   ├── __init__.py
│
├── dashboard/        # Streamlit dashboard UI
│   ├── api.py
│
├── data/             # SQLite database
│   ├── vehicle.db
│
├── database/         # DB connection layer
│   ├── db.py
│   ├── __init__.py
│
├── ml/               # Machine Learning models
│   ├── anomaly_detection.py
│
├── simulator/        # Telemetry data generator
│   ├── telemetry_generator.py
│
└── README.md

🧠 Machine Learning Model
Algorithm: Isolation Forest
Purpose: Detect anomalies in vehicle behavior
Input Features:
Speed
Engine Temperature
Fuel Level
Output:
1 → Normal
-1 → Anomaly

📊 Dashboard Features
Vehicle health score display
Real-time telemetry graphs
System alerts (engine, fuel, speed)
ML anomaly detection table
Clean interactive UI (Streamlit)

🚨 Alert System
Triggers alerts when:
Engine temperature > 95°C
Fuel level < 15%
Speed > 120 km/h
ML detects anomaly

🧮 Health Score Logic
Health score is calculated based on:
Engine temperature stability
Fuel consumption trend
Speed variation
Final score range:
0 (Poor condition) → 100 (Excellent condition)

🛠️ Tech Stack
Python 🐍
Pandas / NumPy
Scikit-learn (ML)
Streamlit (UI Dashboard)
SQLite (Database)

🚀 How to Run
1️⃣ Install dependencies
pip install streamlit pandas numpy scikit-learn
2️⃣ Run dashboard
python -m streamlit run dashboard/api.py

🎯 Use Cases
Automotive companies
Fleet management systems
Predictive vehicle maintenance
Smart mobility systems

💡 Future Improvements
Real-time IoT sensor integration
Cloud deployment (AWS / Azure)
Advanced deep learning models
Live streaming data pipeline

👨‍💻 Author
Mahesh Jadhav

🏆 Project Status
✔ Completed
✔ Working
✔ GitHub Deployed
✔ ML Integrated
✔ Working
✔ GitHub Deployed
✔ ML Integrated

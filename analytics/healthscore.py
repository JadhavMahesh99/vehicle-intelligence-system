import pandas as pd

def calculate_health_score(df):
    score = 100

    if df["engine_temp"].mean() > 90:
        score -= 20

    if df["fuel_level"].diff().mean() < -0.5:
        score -= 20

    if df["speed"].std() > 30:
        score -= 15

    return max(score, 0)
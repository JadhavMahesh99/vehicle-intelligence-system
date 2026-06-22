import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
import time
from datetime import datetime

from database.db import create_table, insert_telemetry


class VehicleTelemetry:

    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.speed = random.randint(20, 60)

    def simulate_speed(self):
        change = random.randint(-10, 15)
        self.speed = max(0, min(140, self.speed + change))
        return self.speed

    def generate_data(self):
        current_speed = self.simulate_speed()

        return {
            "vehicle_id": self.vehicle_id,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "speed": current_speed,
            "rpm": current_speed * random.randint(40, 60),
            "engine_temp": round(
                70 + (current_speed * 0.3) + random.uniform(0, 5), 2
            ),
            "fuel_level": round(
                max(0, 100 - (current_speed * 0.05)), 2
            ),
            "vibration": round(random.uniform(0, 8), 2)
        }


def run_simulation():

    create_table()

    vehicles = [
        VehicleTelemetry("MH12-AX-9988"),
        VehicleTelemetry("MH14-KL-1234"),
        VehicleTelemetry("MH01-ZX-7777")
    ]

    print("🚗 Advanced Vehicle Telemetry System Started...\n")

    while True:

        for vehicle in vehicles:

            data = vehicle.generate_data()

            insert_telemetry(data)

            print(data)

        print("-" * 80)

        time.sleep(2)

if __name__ == "__main__":
    run_simulation()
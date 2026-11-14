
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "Task08_B3" / "input"

INPUT_DIR.mkdir(parents=True, exist_ok=True)

random.seed(42)

HEADERS = [
    "station", "date", "hour",
    "pm25", "pm10", "no2",
    "temperature", "temperature_unit"
]


def generate_dataset(station_count):
    filename = INPUT_DIR / f"air_quality_{station_count}_stations.csv"

    start_date = datetime(2025, 1, 1)
    total_readings = 8760

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)

        for station_number in range(1, station_count + 1):
            station_name = f"Station_{station_number:03d}"

            for hour_index in range(total_readings):
                timestamp = start_date + timedelta(hours=hour_index)

                pm25 = round(random.uniform(5, 180), 2)
                pm10 = round(random.uniform(10, 250), 2)
                no2 = round(random.uniform(5, 100), 2)
                temperature = round(random.uniform(18, 38), 2)

                writer.writerow([
                    station_name,
                    timestamp.strftime("%Y-%m-%d"),
                    timestamp.strftime("%H"),
                    pm25,
                    pm10,
                    no2,
                    temperature,
                    "C"
                ])

    print(f"Generated: {filename.name}")
    print(f"Stations: {station_count}")
    print(f"Readings: {station_count * total_readings:,}")


if __name__ == "__main__":
    for count in [1, 12, 120]:
        generate_dataset(count)

    print("\nAll air-quality datasets generated successfully!")

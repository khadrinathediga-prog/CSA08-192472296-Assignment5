
import csv
import time
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / "output" / "air_quality_cleaned.csv"

# Method 1: Python CSV module
start = time.perf_counter()

station_totals = {}
station_counts = {}

with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        station = row["station"]
        pm25 = float(row["pm25"])

        station_totals[station] = station_totals.get(station, 0) + pm25
        station_counts[station] = station_counts.get(station, 0) + 1

python_results = {
    station: round(station_totals[station] / station_counts[station], 2)
    for station in station_totals
}

python_time = time.perf_counter() - start

# Method 2: Pandas
start = time.perf_counter()

df = pd.read_csv(CSV_FILE)
pandas_results = df.groupby("station")["pm25"].mean().round(2).to_dict()

pandas_time = time.perf_counter() - start

print("Python CSV Results:", python_results)
print("Pandas Results:", pandas_results)

print(f"\nPython CSV execution time: {python_time:.6f} seconds")
print(f"Pandas execution time: {pandas_time:.6f} seconds")

print("\nComparison completed successfully!")


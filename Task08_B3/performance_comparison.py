
import csv
import sqlite3
import time
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "input"

DATASETS = {
    1: INPUT_DIR / "air_quality_1_stations.csv",
    12: INPUT_DIR / "air_quality_12_stations.csv",
    120: INPUT_DIR / "air_quality_120_stations.csv"
}


def python_csv_analysis(file_path):
    totals = {}
    counts = {}

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            station = row["station"]
            pm25 = float(row["pm25"])

            totals[station] = totals.get(station, 0) + pm25
            counts[station] = counts.get(station, 0) + 1

    return {
        station: totals[station] / counts[station]
        for station in totals
    }


def pandas_analysis(file_path):
    df = pd.read_csv(file_path)
    result = df.groupby("station")["pm25"].mean()
    return result.to_dict()


def sqlite_analysis(file_path):
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE air_quality (
            station TEXT,
            pm25 REAL
        )
    """)

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        records = [
            (row["station"], float(row["pm25"]))
            for row in reader
        ]

    cursor.executemany(
        "INSERT INTO air_quality VALUES (?, ?)",
        records
    )

    cursor.execute("""
        SELECT station, AVG(pm25)
        FROM air_quality
        GROUP BY station
    """)

    result = dict(cursor.fetchall())
    connection.close()

    return result


def measure_time(function, file_path):
    start = time.perf_counter()
    result = function(file_path)
    elapsed = time.perf_counter() - start
    return elapsed, result


print("B3 PERFORMANCE COMPARISON")
print("=" * 65)

for station_count, file_path in DATASETS.items():
    print(f"\nDataset: {station_count} station(s)")

    if not file_path.exists():
        print("Dataset not found:", file_path)
        continue

    methods = [
        ("Python CSV", python_csv_analysis),
        ("Pandas", pandas_analysis),
        ("SQLite", sqlite_analysis)
    ]

    for name, function in methods:
        elapsed, result = measure_time(function, file_path)
        print(f"{name:15} : {elapsed:.4f} seconds")

    print("Stations analysed:", len(result))
    print("-" * 65)

print("\nPerformance benchmarking completed!")

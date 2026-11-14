
import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / "output" / "air_quality_cleaned.csv"
DB_FILE = BASE_DIR / "output" / "air_quality.db"


def create_database():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS air_quality (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            station TEXT,
            date TEXT,
            hour TEXT,
            pm25 REAL,
            pm10 REAL,
            no2 REAL,
            temperature REAL
        )
    """)

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        records = [
            (
                row["station"],
                row["date"],
                row["hour"],
                float(row["pm25"]),
                float(row["pm10"]),
                float(row["no2"]),
                float(row["temperature"])
            )
            for row in reader
        ]

    # Clear old records before inserting updated data
    cursor.execute("DELETE FROM air_quality")

    # Insert all cleaned records
    cursor.executemany("""
        INSERT INTO air_quality
        (station, date, hour, pm25, pm10, no2, temperature)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, records)

    connection.commit()

    print("Database created successfully!")
    print(f"Records inserted: {len(records)}")

    print("\n1. Average PM2.5 by station:")
    cursor.execute("""
        SELECT station, ROUND(AVG(pm25), 2)
        FROM air_quality
        GROUP BY station
    """)
    for result in cursor.fetchall():
        print(result)

    print("\n2. Maximum PM10 by station:")
    cursor.execute("""
        SELECT station, MAX(pm10)
        FROM air_quality
        GROUP BY station
    """)
    for result in cursor.fetchall():
        print(result)

    print("\n3. Total readings by station:")
    cursor.execute("""
        SELECT station, COUNT(*)
        FROM air_quality
        GROUP BY station
    """)
    for result in cursor.fetchall():
        print(result)

    connection.close()
    print("\nDatabase analysis completed!")


if __name__ == "__main__":
    create_database()

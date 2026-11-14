
import csv
import statistics
from pathlib import Path

BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / "input" / "air_quality_messy.csv"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_FILE = OUTPUT_DIR / "air_quality_cleaned.csv"

NUMERIC_COLUMNS = ["pm25", "pm10", "no2", "temperature"]

LIMITS = {
    "pm25": (0, 999),
    "pm10": (0, 2000),
    "no2": (0, 1000),
    "temperature": (-50, 60)
}


def clean_data():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    cleaned = []
    seen = set()
    valid_values = {column: [] for column in NUMERIC_COLUMNS}
    duplicate_count = 0

    with open(INPUT_FILE, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        required = {
            "station", "date", "hour", "pm25",
            "pm10", "no2", "temperature", "temperature_unit"
        }

        if not required.issubset(reader.fieldnames or []):
            raise ValueError("Required CSV columns are missing")

        for row in reader:
            try:
                station = (row.get("station") or "").strip().title()
                date = (row.get("date") or "").strip()
                hour = (row.get("hour") or "").strip()

                if not station or not date or not hour:
                    continue

                key = (station, date, hour)

                if key in seen:
                    duplicate_count += 1
                    continue

                seen.add(key)
                values = {}

                for column in NUMERIC_COLUMNS:
                    raw = (row.get(column) or "").strip()

                    if raw.upper() in ("", "NA", "N/A", "NULL"):
                        values[column] = None
                        continue

                    value = float(raw)

                    if column == "temperature":
                        unit = (row.get("temperature_unit") or "").strip().upper()

                        if unit == "F":
                            value = (value - 32) * 5 / 9
                        elif unit != "C":
                            value = None

                    if value is not None:
                        low, high = LIMITS[column]
                        if value < low or value > high:
                            value = None

                    values[column] = value

                for column in NUMERIC_COLUMNS:
                    if values[column] is not None:
                        valid_values[column].append(values[column])

                cleaned.append({
                    "station": station,
                    "date": date,
                    "hour": hour,
                    **values
                })

            except (ValueError, TypeError):
                continue

    medians = {
        column: statistics.median(valid_values[column])
        if valid_values[column] else 0
        for column in NUMERIC_COLUMNS
    }

    previous = {}

    for row in cleaned:
        station = row["station"]

        for column in NUMERIC_COLUMNS:
            key = (station, column)

            if row[column] is None:
                row[column] = previous.get(key, medians[column])

            previous[key] = row[column]
            row[column] = round(row[column], 2)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "station", "date", "hour",
                "pm25", "pm10", "no2", "temperature"
            ]
        )
        writer.writeheader()
        writer.writerows(cleaned)

    print("Air-quality cleaning completed!")
    print(f"Clean records: {len(cleaned)}")
    print(f"Duplicate records removed: {duplicate_count}")
    print(f"Output saved: {OUTPUT_FILE}")


if __name__ == "__main__":
    clean_data()

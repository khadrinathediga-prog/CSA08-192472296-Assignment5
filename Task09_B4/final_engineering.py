
import csv
import sqlite3
import time
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_FILE = (
    BASE_DIR.parent
    / "Task08_B3"
    / "input"
    / "air_quality_120_stations.csv"
)
OUTPUT_DIR = BASE_DIR / "output"
DB_FILE = OUTPUT_DIR / "air_quality.db"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# PART 1: Sentiment analysis of 50 complaints

positive_words = {
    "good", "clean", "fresh", "safe", "excellent",
    "better", "improved", "healthy"
}

negative_words = {
    "bad", "dirty", "polluted", "unsafe", "poor",
    "terrible", "unhealthy", "worse"
}

negations = {"not", "never", "no"}


def analyse_sentiment(text):
    words = text.lower().replace(".", "").replace(",", "").split()
    score = 0
    negate = False

    for word in words:
        if word in negations:
            negate = not negate
            continue

        if word in positive_words:
            score += -1 if negate else 1
            negate = False

        elif word in negative_words:
            score += 1 if negate else -1
            negate = False

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    return "Neutral"


complaints = [
    ("The air is clean and fresh", "Positive"),
    ("The air quality is good", "Positive"),
    ("Pollution levels are terrible", "Negative"),
    ("The air is dirty", "Negative"),
    ("The environment is safe", "Positive"),
    ("The air is polluted", "Negative"),
    ("The air quality is excellent", "Positive"),
    ("The air is unhealthy", "Negative"),
    ("The air is not good", "Negative"),
    ("The air is not bad", "Positive"),
    ("The air is better today", "Positive"),
    ("The air is worse today", "Negative"),
    ("The environment is clean", "Positive"),
    ("The pollution is poor", "Negative"),
    ("The air is not clean", "Negative"),
    ("The air is not polluted", "Positive"),
    ("The air is healthy", "Positive"),
    ("The air is unsafe", "Negative"),
    ("The quality is improved", "Positive"),
    ("The pollution is terrible", "Negative"),
    ("The air is fresh", "Positive"),
    ("The air is not safe", "Negative"),
    ("The air is good and clean", "Positive"),
    ("The air is dirty and polluted", "Negative"),
    ("The air is not unhealthy", "Positive"),
    ("The air quality is worse", "Negative"),
    ("The air quality is better", "Positive"),
    ("The environment is unsafe", "Negative"),
    ("The air is excellent", "Positive"),
    ("The pollution is bad", "Negative"),
    ("The air is not terrible", "Positive"),
    ("The air is not excellent", "Negative"),
    ("The air is clean and safe", "Positive"),
    ("The air is poor and unhealthy", "Negative"),
    ("The air is not dirty", "Positive"),
    ("The air is not fresh", "Negative"),
    ("The environment is healthy", "Positive"),
    ("The pollution is worse", "Negative"),
    ("The air is good today", "Positive"),
    ("The air is bad today", "Negative"),
    ("The air is not worse", "Positive"),
    ("The air is not healthy", "Negative"),
    ("The air quality improved", "Positive"),
    ("The air quality is terrible today", "Negative"),
    ("The environment is safe and clean", "Positive"),
    ("The air is polluted and unsafe", "Negative"),
    ("The air is not poor", "Positive"),
    ("The air is not fresh today", "Negative"),
    ("The air is excellent and healthy", "Positive"),
    ("The air is dirty and unhealthy", "Negative")
]


def test_complaints():
    correct = 0

    print("\n50 COMPLAINT SENTIMENT ANALYSIS")
    print("-" * 50)

    for complaint, manual_label in complaints:
        predicted = analyse_sentiment(complaint)

        if predicted == manual_label:
            correct += 1

    agreement = correct / len(complaints) * 100

    print("Total complaints:", len(complaints))
    print("Correct predictions:", correct)
    print("Incorrect predictions:", len(complaints) - correct)
    print(f"Agreement with manual labels: {agreement:.2f}%")


# PART 2: SQLite indexing and query timing

def test_database_indexing():
    if not DATA_FILE.exists():
        print("B3 dataset not found:", DATA_FILE)
        return

    if DB_FILE.exists():
        DB_FILE.unlink()

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE air_quality (
            station TEXT,
            date TEXT,
            hour TEXT,
            pm25 REAL,
            pm10 REAL,
            no2 REAL,
            temperature REAL
        )
    """)

    print("\nLoading 120-station dataset into SQLite...")

    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        while True:
            batch = []

            for _ in range(10000):
                row = next(reader, None)

                if row is None:
                    break

                batch.append((
                    row["station"],
                    row["date"],
                    row["hour"],
                    float(row["pm25"]),
                    float(row["pm10"]),
                    float(row["no2"]),
                    float(row["temperature"])
                ))

            if not batch:
                break

            cursor.executemany("""
                INSERT INTO air_quality
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, batch)

    connection.commit()

    query = """
        SELECT AVG(pm25)
        FROM air_quality
        WHERE station = ? AND date = ?
    """

    parameters = ("Station_001", "2025-01-01")

    # Measure query without index
    start = time.perf_counter()

    for _ in range(100):
        cursor.execute(query, parameters)
        cursor.fetchone()

    without_index = (time.perf_counter() - start) / 100

    # Create composite index
    cursor.execute("""
        CREATE INDEX idx_station_date
        ON air_quality(station, date)
    """)

    connection.commit()

    # Measure query with index
    start = time.perf_counter()

    for _ in range(100):
        cursor.execute(query, parameters)
        cursor.fetchone()

    with_index = (time.perf_counter() - start) / 100

    print("\nSQLITE INDEX PERFORMANCE")
    print("Query time without index:", f"{without_index:.6f}", "seconds")
    print("Query time with index:", f"{with_index:.6f}", "seconds")

    if with_index < without_index:
        print("Index improved query performance.")
    else:
        print("Index did not improve this measured query.")

    cursor.execute("SELECT COUNT(*) FROM air_quality")
    print("Total database readings:", cursor.fetchone()[0])

    connection.close()


if __name__ == "__main__":
    test_complaints()
    test_database_indexing()

    print("\nB4 engineering investigation completed!")

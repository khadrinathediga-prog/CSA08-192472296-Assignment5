
import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "input"
INPUT_DIR.mkdir(parents=True, exist_ok=True)


# 1. Create adversarial CSV test files
def create_test_files():
    # Missing column
    with open(INPUT_DIR / "missing_column.csv", "w", newline="") as file:
        file.write("station,date,pm25\nAdyar,2026-10-01,48\n")

    # Wrong delimiter
    with open(INPUT_DIR / "wrong_delimiter.csv", "w", newline="") as file:
        file.write("station;date;pm25\nAdyar;2026-10-01;48\n")

    # Different encoding
    with open(INPUT_DIR / "different_encoding.csv", "w", encoding="utf-16") as file:
        file.write("station,date,pm25\nAdyar,2026-10-01,48\n")

    # Empty CSV
    with open(INPUT_DIR / "empty.csv", "w") as file:
        pass


# 2. Test adversarial CSV files
def test_csv_files():
    print("\nCSV ADVERSARIAL TESTING")

    required_columns = {"station", "date", "hour", "pm25"}

    for filename in [
        "missing_column.csv",
        "wrong_delimiter.csv",
        "different_encoding.csv",
        "empty.csv"
    ]:
        path = INPUT_DIR / filename

        try:
            with open(path, "r", encoding="utf-8", newline="") as file:
                reader = csv.DictReader(file)
                headers = reader.fieldnames or []

                if not headers:
                    print(filename, "REJECTED: Empty file")
                elif not required_columns.issubset(headers):
                    print(filename, "REJECTED: Missing columns or wrong delimiter")
                else:
                    print(filename, "ACCEPTED")

        except (UnicodeError, csv.Error, OSError) as error:
            print(filename, "REJECTED:", error)


# 3. SQL injection testing
def test_sql_injection():
    print("\nSQL INJECTION TESTING")

    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE air_quality (
            station TEXT,
            pm25 REAL
        )
    """)

    records = [
        ("Adyar", 48.0),
        ("Guindy", 108.0)
    ]

    cursor.executemany(
        "INSERT INTO air_quality VALUES (?, ?)",
        records
    )
    connection.commit()

    malicious_input = "' OR '1'='1' --"

    # Unsafe query demonstration
    unsafe_query = (
        "SELECT station, pm25 FROM air_quality "
        f"WHERE station = '{malicious_input}'"
    )

    cursor.execute(unsafe_query)
    unsafe_results = cursor.fetchall()

    print("Unsafe query results:", unsafe_results)

    # Safe parameterised query
    cursor.execute(
        "SELECT station, pm25 FROM air_quality WHERE station = ?",
        (malicious_input,)
    )

    safe_results = cursor.fetchall()

    print("Safe query results:", safe_results)

    print("SQL injection prevented using parameterised query:", len(safe_results) == 0)

    connection.close()


if __name__ == "__main__":
    create_test_files()
    test_csv_files()
    test_sql_injection()

    print("\nAdversarial testing completed!")

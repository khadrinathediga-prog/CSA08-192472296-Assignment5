
import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# Create table
cursor.execute("""
    CREATE TABLE air_quality (
        station TEXT,
        pm25 REAL
    )
""")

# Sample records
records = [
    ("Adyar", 54.0),
    ("Guindy", 108.0),
    ("Velachery", 72.0)
]

# TODO 1: Insert records using executemany and placeholders
cursor.executemany(
    "INSERT INTO air_quality (station, pm25) VALUES (?, ?)",
    records
)

connection.commit()

print("Records inserted successfully!")

# TODO 2: Parameterised SELECT query
station_name = "Adyar"

cursor.execute(
    "SELECT station, pm25 FROM air_quality WHERE station = ?",
    (station_name,)
)

print("\nStation reading:")
print(cursor.fetchone())

# Test SQL injection input
malicious_input = "' OR '1'='1' --"

cursor.execute(
    "SELECT station, pm25 FROM air_quality WHERE station = ?",
    (malicious_input,)
)

print("\nSQL injection test:")
print("Result:", cursor.fetchall())

connection.close()

print("\nParameterized SQL testing completed!")

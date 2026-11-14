
import sqlite3
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).parent
DB_FILE = BASE_DIR / "output" / "air_quality.db"
OUTPUT_DIR = BASE_DIR / "output" / "charts"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# 1. Station-wise PM2.5 comparison
cursor.execute("""
    SELECT station, AVG(pm25)
    FROM air_quality
    GROUP BY station
""")
data = cursor.fetchall()

stations = [row[0] for row in data]
averages = [row[1] for row in data]

plt.figure()
plt.bar(stations, averages)
plt.title("Average PM2.5 by Station")
plt.xlabel("Station")
plt.ylabel("Average PM2.5")
plt.savefig(OUTPUT_DIR / "station_comparison.png")
plt.close()

# 2. Monthly PM2.5 trend
cursor.execute("""
    SELECT substr(date, 1, 7), AVG(pm25)
    FROM air_quality
    GROUP BY substr(date, 1, 7)
    ORDER BY substr(date, 1, 7)
""")
data = cursor.fetchall()

months = [row[0] for row in data]
monthly_values = [row[1] for row in data]

plt.figure()
plt.plot(months, monthly_values, marker="o")
plt.title("Monthly PM2.5 Trend")
plt.xlabel("Month")
plt.ylabel("Average PM2.5")
plt.savefig(OUTPUT_DIR / "monthly_trend.png")
plt.close()

# 3. Temperature vs PM2.5
cursor.execute("""
    SELECT temperature, pm25
    FROM air_quality
""")
data = cursor.fetchall()

temperatures = [row[0] for row in data]
pm25_values = [row[1] for row in data]

plt.figure()
plt.scatter(temperatures, pm25_values)
plt.title("Temperature vs PM2.5")
plt.xlabel("Temperature (Celsius)")
plt.ylabel("PM2.5")
plt.savefig(OUTPUT_DIR / "temperature_vs_pm25.png")
plt.close()

# 4. PM2.5 distribution
cursor.execute("SELECT pm25 FROM air_quality")
pm25_values = [row[0] for row in cursor.fetchall()]

plt.figure()
plt.hist(pm25_values, bins=5)
plt.title("PM2.5 Distribution")
plt.xlabel("PM2.5")
plt.ylabel("Frequency")
plt.savefig(OUTPUT_DIR / "pm25_distribution.png")
plt.close()

connection.close()

print("All four visualisations generated successfully!")
print(f"Charts saved in: {OUTPUT_DIR}")

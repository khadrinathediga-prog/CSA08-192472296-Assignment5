# A1 – Data Acquisition

## 1. Introduction

Data acquisition is the process of collecting air-quality readings from multiple monitoring stations for further processing and analysis.

The City Air Quality Monitoring Network contains 12 monitoring stations.

The dataset includes:

- Date
- Hour
- PM2.5
- PM10
- NO2
- Temperature
- Temperature unit

## 2. Data Sources

Two data storage approaches are considered.

### A. CSV Files

CSV (Comma-Separated Values) files store air-quality readings in a tabular format.

**Advantages:**
- Easy to create and maintain.
- Simple to import into Python.
- Portable and readable.
- Suitable for small and medium datasets.

**Disadvantages:**
- Limited support for concurrent access.
- Searching large files can be slow.
- No built-in indexing.

### B. SQL Database

An SQL database stores structured information in tables and supports queries using SQL.

**Advantages:**
- Supports structured data storage.
- Provides efficient filtering and aggregation.
- Supports indexing.
- Supports data integrity and concurrent access.

**Disadvantages:**
- Requires database configuration.
- Requires SQL knowledge.
- Additional database maintenance.

## 3. Data Acquisition Methods

### CSV Using Python

Python's CSV module can read records sequentially.

```python
import csv

with open("air_quality.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

### SQL Database Query

SQL can retrieve specific station readings.

```sql
SELECT *
FROM air_quality
WHERE station = 'Adyar';
```

## 4. Complexity Analysis

| Method | Time Complexity |
|---|---|
| Full CSV scan | O(n) |
| SQL indexed lookup | Approximately O(log n) |

Here, n represents the number of records.

A full CSV scan checks records sequentially. An indexed SQL query can locate matching records more efficiently, depending on the index and query.

## 5. Alternative Approach: Pandas

Pandas can load CSV data into a DataFrame and perform filtering and analysis.

```python
import pandas as pd

data = pd.read_csv("air_quality.csv")

adyar_data = data[data["station"] == "Adyar"]

print(adyar_data)
```

Pandas is useful for data analysis, filtering, grouping, and aggregation. However, loading an entire large CSV file into memory may require significant memory resources.

## 6. Comparison

| Feature | CSV | SQL | Pandas |
|---|---|---|---|
| Data storage | File | Database | DataFrame |
| Searching | Sequential scan | Indexed query | DataFrame filtering |
| Analysis | Basic | SQL aggregation | Advanced analysis |
| Indexing | Not built-in | Supported | Supported through DataFrame indexes |
| Best use | Data exchange | Structured storage | Data analysis |

## 7. Conclusion

CSV files are suitable for collecting and exchanging air-quality readings. SQL databases provide structured storage and indexed retrieval, while Pandas supports efficient data analysis.

For the City Air Quality Monitoring Network, CSV can be used for initial data collection, SQL for structured storage, and Pandas for analytical processing.
## 7. Pseudocode – Air Quality Data Acquisition

```text
ALGORITHM Acquire_Air_Quality_Data(file)

BEGIN
    OPEN file in read mode

    IF file does not exist THEN
        DISPLAY "File not found"
        STOP
    END IF

    READ column headers

    IF required columns are missing THEN
        DISPLAY "Invalid dataset"
        CLOSE file
        STOP
    END IF

    FOR each record IN file DO
        READ station, date, hour, PM2.5, PM10, NO2, temperature
        STORE record in dataset
    END FOR

    CLOSE file
    RETURN dataset
END
```
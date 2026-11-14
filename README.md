# Python Programming Assignment 5 – CO5

## Student Details

- **Name:** Khadrinath Gowd
- **Register Number:** 192472296
- **Course:** B.Tech – CSE (AI)
- **Python Version:** 3.13.9
- **GitHub Username:** khadrinathediga-prog

## Project Title

**City Air Quality Monitoring Network – Data Processing and Analysis**

## Project Description

This project focuses on collecting, cleaning, analysing, and processing air-quality data from multiple monitoring stations.

The dataset contains PM2.5, PM10, NO2, temperature, date, and hourly readings.

The project uses Python, CSV, Pandas, SQLite, and Matplotlib to perform data processing, database operations, performance comparisons, and visualisation.

## Project Folder Structure

```text
CSA08-192472296-Assignment5/
│
├── generate_data.py
├── README.md
│
├── Task01_A1/
├── Task02_A2/
├── Task03_A3/
├── Task04_A4/
├── Task05_A5/
├── Task06_B1/
│   ├── input/
│   ├── output/
│   │   └── charts/
│   ├── screenshots/
│   ├── cleaning_pipeline.py
│   ├── database_analysis.py
│   ├── visualization.py
│   └── pandas_comparison.py
│
├── Task07_B2/
├── Task08_B3/
└── Task09_B4/
```

## Software and Libraries

- Python 3.13.9
- CSV
- SQLite3
- Pandas
- Matplotlib
- Statistics
- pathlib
- time

## Task B1 – Implementation and Results

### 1. Data Cleaning

Implemented a Python cleaning pipeline to handle:

- Missing values
- Negative and impossible readings
- Duplicate records
- Fahrenheit-to-Celsius conversion
- Missing-value replacement using forward fill and median

### 2. SQLite Database

Created an SQLite database and inserted cleaned records using `executemany()`.

Implemented three SQL queries:

1. Average PM2.5 by station.
2. Maximum PM10 by station.
3. Total readings by station.

### 3. Data Visualisation

Generated four charts:

- Station-wise PM2.5 comparison
- Monthly PM2.5 trend
- Temperature vs PM2.5 scatter plot
- PM2.5 distribution histogram

### 4. Python CSV vs Pandas

Compared Python CSV processing with Pandas groupby operations.

Both methods produced identical average PM2.5 results.

| Station | Average PM2.5 |
|---|---:|
| Adyar | 48.0 |
| Guindy | 95.0 |

Execution time on the small test dataset:

- Python CSV: 0.000269 seconds
- Pandas: 0.004219 seconds

### 5. Invalid Data Testing

Tested an impossible PM2.5 reading of 1200.

The cleaning pipeline rejected the invalid measurement and replaced it with a valid value while retaining the record.

### Final B1 Database Results

| Metric | Adyar | Guindy |
|---|---:|---:|
| Average PM2.5 | 48.0 | 95.0 |
| Maximum PM10 | 90.0 | 140.0 |
| Total readings | 4 | 3 |

Total cleaned records: **7**

## Execution Commands

Run these commands from the main project directory:

```bash
python3 generate_data.py
python3 Task06_B1/cleaning_pipeline.py
python3 Task06_B1/database_analysis.py
python3 Task06_B1/visualization.py
python3 Task06_B1/pandas_comparison.py
```

## Conclusion

The B1 implementation demonstrates data cleaning, data normalisation, SQLite database operations, SQL aggregation, data visualisation, and performance comparison between Python CSV and Pandas.

Further tasks will be documented as their implementations are completed.
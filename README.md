# Python Programming Assignment 5 – CO5

## Student Details

| Field | Details |
|---|---|
| Student Name | Khadrinath Gowd |
| Register Number | 192472296 |
| Course | B.Tech – CSE (AI) |
| Assignment | Python Programming Assignment 5 |
| Course Outcome | CO5 |
| Python Version | 3.13.9 |

## Project Title

**City Air Quality Monitoring Network – Data Processing, Analysis, Performance Evaluation and AI Application Design**

## Project Overview

This project develops a data-processing and analysis solution for a city air-quality monitoring network containing 12 monitoring stations.

The system handles daily air-quality readings such as PM2.5, PM10, NO2 and temperature. It addresses missing values, duplicate records, invalid measurements, inconsistent temperature units and citizen complaints.

The assignment also investigates Python CSV processing, Pandas, SQLite database operations, performance profiling, sentiment analysis and AI application design.

## Technologies and Libraries

| Technology | Version / Details |
|---|---|
| Python | 3.13.9 |
| Pandas | 2.3.3 |
| Matplotlib | 3.10.9 |
| SQLite | Python built-in sqlite3 |
| CSV | Python built-in csv module |
| cProfile | Python built-in profiler |
| timeit / perf_counter | Python built-in timing tools |

## Project Structure

```text
CSA08-192472296-Assignment5/
│
├── README.md
├── .gitignore
├── generate_data.py
│
├── Task01_A1/
│   └── data_acquisition.md
│
├── Task02_A2/
│   └── data_cleaning.md
│
├── Task03_A3/
│   └── data_analysis.md
│
├── Task04_A4/
│   └── debugging_profiling.md
│
├── Task05_A5/
│   └── ai_application_design.md
│
├── Task06_B1/
│   ├── input/
│   ├── output/
│   ├── screenshots/
│   ├── cleaning_pipeline.py
│   ├── database_analysis.py
│   ├── visualization.py
│   └── pandas_comparison.py
│
├── Task07_B2/
│   ├── input/
│   ├── screenshots/
│   ├── adversarial_tests.py
│   ├── sentiment_analysis.py
│   └── parameterized_sql.py
│
├── Task08_B3/
│   ├── input/
│   ├── screenshots/
│   ├── performance_comparison.py
│   └── profiling.py
│
└── Task09_B4/
    ├── output/
    ├── screenshots/
    ├── final_engineering.py
    └── engineering_decision.md
```

## Part A – Data and Program Design

### A1 – Data Acquisition
- Studied CSV, SQL and Pandas data acquisition methods.
- Designed the air-quality data acquisition process.
- Included algorithmic complexity and pseudocode.

### A2 – Data Cleaning and Normalisation
- Identified missing and invalid values.
- Removed duplicate records.
- Converted Fahrenheit temperatures into Celsius.
- Applied forward filling and median replacement.
- Included normalisation methods and pseudocode.

### A3 – Data Analysis and Visualisation
- Analysed station-wise air-quality readings.
- Designed SQL aggregation queries.
- Studied data visualisation methods.
- Included pseudocode and complexity analysis.

### A4 – Debugging and Profiling
- Studied print debugging, assertions, logging and Python debugger.
- Used execution-time measurement and profiling concepts.
- Included pseudocode and debugging strategies.

### A5 – AI Application Design
- Designed sentiment analysis for citizen complaints.
- Proposed extractive text summarisation.
- Designed a rule-based air-quality chatbot.
- Compared rule-based and machine-learning approaches.

## Part B – Implementation and Experimental Investigation

### B1 – Cleaning Pipeline and Database Analysis

Implemented:
- CSV data cleaning and validation.
- Duplicate removal and missing-value handling.
- Temperature unit conversion.
- SQLite database insertion using `executemany()`.
- SQL aggregation queries.
- Four data visualisations.
- Python CSV versus Pandas comparison.

**Cleaning result:**
- Cleaned records: 7
- Duplicate records removed: 1
- Invalid measurements handled through validation and replacement.

### B2 – Adversarial Data and SQL Security

Implemented:
- Missing-column CSV testing.
- Wrong-delimiter testing.
- Different-encoding testing.
- Empty-file testing.
- SQL injection testing.
- Parameterised SQL queries.
- `executemany()` database insertion.
- Rule-based sentiment analysis with negation handling.

The SQL injection test demonstrated the difference between unsafe query construction and parameterised queries.

### B3 – Performance Comparison and Profiling

Compared three approaches:

1. Python CSV processing.
2. Pandas groupby.
3. SQLite GROUP BY.

Datasets contained 1, 12 and 120 monitoring stations, with 8,760 readings per station.

**Observed benchmark results from one execution:**

| Stations | Python CSV | Pandas | SQLite |
|---:|---:|---:|---:|
| 1 | 0.0175 s | 0.0160 s | 0.0278 s |
| 12 | 0.2042 s | 0.0670 s | 0.3073 s |
| 120 | 2.0605 s | 0.6372 s | 3.1954 s |

Pandas performed fastest in these particular tests. Actual execution times may vary depending on hardware and system load.

Python cProfile was used to identify time-consuming functions.

### B4 – Final Engineering Decision

Implemented:
- Sentiment analysis of 50 citizen complaints.
- Comparison against predefined manual labels.
- SQLite database testing with 1,051,200 readings.
- Composite indexing on `(station, date)`.
- Query performance comparison with and without the index.
- Production architecture recommendation.

**Observed results:**
- Total complaints: 50
- Correct predictions against predefined labels: 50
- Agreement with manual labels: 100%
- Query time without index: 0.065486 seconds
- Query time with index: 0.000011 seconds

The 100% agreement represents the tested sample only and should not be interpreted as real-world model accuracy.

## Installation

Clone the repository:

```bash
git clone https://github.com/khadrinathediga-prog/CSA08-192472296-Assignment5.git
```

Move into the project directory:

```bash
cd CSA08-192472296-Assignment5
```

Install required external libraries:

```bash
python3 -m pip install pandas matplotlib
```

## Execution Commands

Run commands from the project root directory.

**Generate performance datasets:**

```bash
python3 generate_data.py
```

**B1 – Cleaning pipeline:**

```bash
python3 Task06_B1/cleaning_pipeline.py
```

**B1 – Database analysis:**

```bash
python3 Task06_B1/database_analysis.py
```

**B1 – Visualisation:**

```bash
python3 Task06_B1/visualization.py
```

**B1 – Pandas comparison:**

```bash
python3 Task06_B1/pandas_comparison.py
```

**B2 – Adversarial testing:**

```bash
python3 Task07_B2/adversarial_tests.py
```

**B2 – Sentiment analysis:**

```bash
python3 Task07_B2/sentiment_analysis.py
```

**B2 – Parameterised SQL:**

```bash
python3 Task07_B2/parameterized_sql.py
```

**B3 – Performance comparison:**

```bash
python3 Task08_B3/performance_comparison.py
```

**B3 – Profiling:**

```bash
python3 Task08_B3/profiling.py
```

**B4 – Final engineering investigation:**

```bash
python3 Task09_B4/final_engineering.py
```

## Screenshots and Evidence

Screenshots of program execution, cleaning results, SQL analysis, charts, adversarial testing, sentiment analysis, performance benchmarks and profiling are stored in the corresponding task folders.

## Engineering Conclusion

The project demonstrates an end-to-end workflow for processing air-quality data, cleaning inconsistent records, performing database analysis, visualising pollution trends and evaluating processing performance.

Pandas provided efficient aggregation for the tested datasets. SQLite supported structured storage and indexed queries. Parameterised SQL improved database security.

For a larger production monitoring network, the recommended architecture combines scheduled data ingestion, automated validation,
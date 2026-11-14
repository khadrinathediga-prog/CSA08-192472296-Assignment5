# PYTHON PROGRAMMING ASSIGNMENT 5 – CO5

## City Air Quality Monitoring Network

### Student Details

| Particulars | Details |
|---|---|
| Student Name | Khadrinath Gowd |
| Register Number | 192472296 |
| Department | B.Tech – Computer Science and Engineering (AI) |
| Assignment | Python Programming Assignment 5 |
| Course Outcome | CO5 |
| Python Version | 3.13.9 |

---

# 1. Introduction

The City Air Quality Monitoring Network project focuses on collecting, cleaning, analysing and processing air-quality data from multiple monitoring stations.

The dataset contains information such as date, hour, PM2.5, PM10, NO2 and temperature. The project addresses practical challenges including missing values, duplicate records, invalid measurements, inconsistent temperature units and citizen complaints.

Python, Pandas, Matplotlib and SQLite are used to implement data processing, database analysis, visualisation and performance evaluation.

# 2. Objectives

- Understand different data acquisition methods.
- Clean and normalise air-quality datasets.
- Analyse data using Python, Pandas and SQL.
- Generate meaningful visualisations.
- Apply debugging and profiling techniques.
- Design AI-assisted applications for citizen complaints.
- Test adversarial datasets and SQL injection scenarios.
- Compare the performance of different processing approaches.
- Develop a final engineering recommendation.

# 3. Part A – Data and Program Design

## A1. Data Acquisition

Studied CSV files, SQL databases and Pandas as data acquisition and processing approaches.

The comparison considered data storage, searching, indexing, analysis and computational complexity.

A pseudocode algorithm was developed to acquire air-quality readings and validate the required columns.

## A2. Data Cleaning and Normalisation

Studied data-cleaning techniques for handling:

- Missing values
- Duplicate records
- Negative and impossible measurements
- Temperature conversion from Fahrenheit to Celsius
- Forward filling and median replacement
- Min-max normalisation and z-score normalisation

A pseudocode algorithm was developed for the cleaning process.

## A3. Data Analysis and Visualisation

Studied station-wise pollution analysis, SQL aggregation and graphical representation.

The analysis considered average PM2.5, station comparisons, pollution trends and temperature relationships.

A pseudocode algorithm was developed for aggregating station readings and generating charts.

## A4. Debugging and Profiling

Studied debugging techniques including:

- Print debugging
- Assertions
- Logging
- Python debugger
- Execution-time measurement
- cProfile and profiling

A pseudocode algorithm was developed to explain the debugging and profiling process.

## A5. AI Application Design

Designed three AI-assisted applications:

1. Sentiment analysis of citizen complaints.
2. Extractive text summarisation.
3. Rule-based chatbot for air-quality information.

Also compared rule-based approaches with machine-learning approaches and discussed their limitations.

# 4. Part B – Implementation and Experimental Investigation

## B1. Cleaning Pipeline and Database Analysis

Implemented a Python-based cleaning pipeline.

Major operations included:
- Reading CSV datasets.
- Validating required columns.
- Removing duplicate records.
- Handling missing values.
- Converting Fahrenheit to Celsius.
- Validating measurement ranges.
- Saving cleaned output.

SQLite was used for structured storage and SQL aggregation.

Four visualisations were generated:
- Station comparison.
- Monthly trend.
- Temperature versus PM2.5.
- PM2.5 distribution.

Python CSV processing was also compared with Pandas aggregation.

**Observed cleaning results:**

| Metric | Result |
|---|---:|
| Cleaned records | 7 |
| Duplicate records removed | 1 |
| Remaining duplicate records | 0 |

## B2. Adversarial Data and SQL Security

Tested the system using different adversarial CSV inputs:

- Missing columns.
- Incorrect delimiters.
- Different file encoding.
- Empty files.

SQL injection testing compared unsafe SQL construction with parameterised SQL queries.

The implementation also used `executemany()` for database insertion and included sentiment analysis with negation handling.

The tests demonstrated the importance of input validation and parameterised database operations.

## B3. Performance Comparison and Profiling

Compared three data-processing approaches:

1. Python CSV.
2. Pandas groupby.
3. SQLite GROUP BY.

The generated datasets contained 1, 12 and 120 monitoring stations, with 8,760 readings per station.

### Experimental Results

| Stations | Python CSV | Pandas | SQLite |
|---:|---:|---:|---:|
| 1 | 0.0175 s | 0.0160 s | 0.0278 s |
| 12 | 0.2042 s | 0.0670 s | 0.3073 s |
| 120 | 2.0605 s | 0.6372 s | 3.1954 s |

Pandas provided the fastest execution time in these particular experiments.

Python cProfile was used to identify time-consuming functions and investigate performance bottlenecks.

*Note: Execution times may vary depending on hardware and system load.*

## B4. Final Engineering Investigation

Implemented sentiment analysis for 50 citizen complaints and compared the predicted labels with predefined manual labels.

A SQLite database containing 1,051,200 readings was used for query performance testing.

A composite index was created on `(station, date)`.

### Sentiment Analysis Results

| Metric | Result |
|---|---:|
| Total complaints | 50 |
| Correct predictions against manual labels | 50 |
| Incorrect predictions | 0 |
| Agreement with manual labels | 100% |

The 100% agreement applies only to the predefined test sample and does not represent validated real-world model accuracy.

### Database Performance Results

| Measurement | Execution Time |
|---|---:|
| Query without index | 0.065486 seconds |
| Query with index | 0.000011 seconds |

The indexed query was significantly faster in the tested experiment.

# 5. Final Engineering Decision

For a larger air-quality monitoring network, the recommended system should combine:

- Automated data ingestion.
- Data validation and cleaning.
- Pandas for analytical processing.
- SQLite for structured storage and indexed queries in the tested setup.
- Appropriate database scaling for larger production workloads.
- NLP-based complaint processing.
- Human review for uncertain sentiment predictions.

For a network with 100 or more stations, readings every 15 minutes and approximately 50,000 complaints per month, the system should be designed with scalable storage, efficient indexing and automated processing.

# 6. Tools and Technologies Used

| Tool / Technology | Version or Usage |
|---|---|
| Python | 3.13.9 |
| Pandas | 2.3.3 |
| Matplotlib | 3.10.9 |
| SQLite | Python sqlite3 |
| CSV | Python csv module |
| cProfile | Performance profiling |
| VS Code | Development environment |
| Git and GitHub | Version control and project hosting |

# 7. Screenshots and Evidence

Execution screenshots are organised in the corresponding task folders.

- Task01_A1 – Data acquisition evidence.
- Task02_A2 – Data cleaning evidence.
- Task03_A3 – Data analysis evidence.
- Task04_A4 – Debugging and profiling evidence.
- Task05_A5 – AI application design evidence.
- Task06_B1 – Cleaning pipeline, SQL analysis and visualisation.
- Task07_B2 – Adversarial testing, sentiment analysis and SQL security.
- Task08_B3 – Performance comparison and profiling.
- Task09_B4 – Final engineering investigation.

# 8. Conclusion

The Python Programming Assignment 5 demonstrates an end-to-end approach to air-quality data acquisition, cleaning, analysis, database management, visualisation and performance evaluation.

The implementation demonstrates how Python, Pandas and SQLite can be combined to process monitoring data. Adversarial testing highlights the importance of data validation and SQL security. Performance experiments demonstrate the effect of processing methods and database indexing.

The project also explores AI-assisted sentiment analysis, text summarisation and chatbot design for citizen complaint management.

Overall, the assignment provides practical experience in Python programming, data engineering, database operations, performance analysis and AI application design.

---

## GitHub Repository

https://github.com/khadrinathediga-prog/CSA08-192472296-Assignment5
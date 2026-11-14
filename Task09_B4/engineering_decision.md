# B4 – Final Engineering Decision

## 1. Project Overview

The City Air Quality Monitoring Network collects air-quality readings from multiple monitoring stations. The system must process large amounts of data, analyse pollution levels, and handle citizen complaints.

The production system is expected to support:

- More than 100 monitoring stations.
- Air-quality readings every 15 minutes.
- Approximately 50,000 citizen complaints per month.

## 2. Experimental Results

### A. Performance Comparison

Three approaches were tested using datasets containing 1, 12, and 120 stations.

| Dataset | Python CSV | Pandas | SQLite |
|---|---:|---:|---:|
| 1 station | 0.0175 s | 0.0160 s | 0.0278 s |
| 12 stations | 0.2042 s | 0.0670 s | 0.3073 s |
| 120 stations | 2.0605 s | 0.6372 s | 3.1954 s |

**Observation:** Pandas performed fastest in the experiments, particularly with the 120-station dataset.

### B. Sentiment Analysis

A rule-based sentiment analyser was tested using 50 citizen complaints.

- Total complaints: 50
- Correct predictions: 50
- Incorrect predictions: 0
- Agreement with manual labels: 100%

This result applies to the predefined test dataset. Real-world complaints may contain sarcasm, spelling errors, and complex language.

### C. SQLite Indexing

A composite index was created on `(station, date)`.

| Measurement | Query time |
|---|---:|
| Without index | 0.065486 seconds |
| With index | 0.000011 seconds |

**Observation:** The index significantly reduced the measured query time for the tested station and date query.

## 3. Final Engineering Decisions

### Data Processing

Use Pandas for batch processing, data cleaning, aggregation, and analysis because it performed well in the experimental comparison.

For larger datasets, process data in batches to manage memory consumption.

### Database

Use SQLite for the prototype and local analytical operations.

For a larger production deployment with concurrent users and continuous incoming readings, consider a server-based relational database.

Create indexes on frequently queried columns such as station and date.

### Complaint Analysis

Use rule-based sentiment analysis as an initial classification method.

For production, improve the system using a machine-learning or NLP model that can handle sarcasm, negation, mixed sentiment, and complex language.

Keep human review available for uncertain or important complaints.

### Data Collection

Collect readings every 15 minutes and validate incoming records before storing them.

Apply automated checks for missing values, duplicate readings, invalid measurements, and temperature-unit conversion.

## 4. Scalability and Reliability

For a network with more than 100 stations and 50,000 complaints per month:

1. Use batch processing for large datasets.
2. Use database indexing for frequently accessed records.
3. Store cleaned and validated readings separately from raw data.
4. Automate data validation and error logging.
5. Monitor processing time and database performance.
6. Evaluate the production system using larger datasets and concurrent workloads.

## 5. Conclusion

Based on the experimental results, Pandas is a suitable choice for data analysis, while SQLite indexing improves query performance for the tested workload.

A combination of automated data cleaning, indexed database storage, efficient data processing, and improved NLP-based complaint analysis is recommended for the City Air Quality Monitoring Network.

The final architecture should be tested under realistic production workloads before deployment.
# A3 – Data Analysis and Visualisation

## 1. Introduction

Data analysis helps identify air-pollution patterns, station-wise differences, and relationships between environmental measurements.

Data visualisation presents the findings using charts and graphs.

## 2. Analysis Requirements

### A. Monthly PM2.5 Trend

A line chart displays average PM2.5 readings over time.

**Purpose:** Identify pollution trends and changes across months.

### B. Station Comparison

A bar chart compares average PM2.5 values across monitoring stations.

**Purpose:** Identify stations with higher pollution levels.

### C. Temperature vs PM2.5

A scatter plot represents the relationship between temperature and PM2.5.

**Purpose:** Observe whether temperature changes are associated with pollution levels.

### D. Worst Pollution Hours

A histogram or box plot helps identify the distribution of PM2.5 readings and periods with higher pollution.

**Purpose:** Identify unusual pollution readings and distribution patterns.

## 3. Daily Summary Table

The system generates a daily summary containing:

- Minimum PM2.5
- Maximum PM2.5
- Average PM2.5
- Total number of readings

Example SQL query:

```sql
SELECT
    station,
    date,
    MIN(pm25),
    MAX(pm25),
    ROUND(AVG(pm25), 2),
    COUNT(*)
FROM air_quality
GROUP BY station, date;
```

## 4. Alternative Approach: SQL vs Python

### Python Processing

Python loops can calculate averages, minimums, and maximums by processing records individually.

### SQL Processing

SQL uses aggregate functions such as:

- AVG()
- MIN()
- MAX()
- COUNT()
- GROUP BY

SQL can perform aggregation directly within the database.

## 5. Complexity Analysis

| Operation | Time Complexity |
|---|---|
| Full data scan | O(n) |
| Average calculation | O(n) |
| Minimum and maximum | O(n) |
| Grouping and aggregation | Depends on data and database implementation |

## 6. Conclusion

Data analysis and visualisation help understand air-quality patterns and identify highly polluted stations.

Line charts, bar charts, scatter plots, and histograms provide different perspectives on air-quality measurements. SQL aggregation and Python analysis support efficient reporting and decision-making.
## 7. Pseudocode – Air Quality Data Analysis

```text
ALGORITHM Analyse_Air_Quality(dataset)

BEGIN
    INITIALISE station totals and reading counts

    FOR each record IN dataset DO
        station ← record.station
        ADD record.PM2.5 to station total
        INCREMENT station reading count
    END FOR

    FOR each station DO
        average ← station total / reading count
        DISPLAY station and average
    END FOR

    GENERATE charts for:
        Station-wise pollution comparison
        Monthly pollution trends
        Temperature versus PM2.5
        PM2.5 distribution

    SAVE analysis results and charts
END
```
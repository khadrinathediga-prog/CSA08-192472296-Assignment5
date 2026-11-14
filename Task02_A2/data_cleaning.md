# A2 – Data Cleaning and Normalisation

## 1. Introduction

Data cleaning is the process of identifying and correcting missing, duplicate, invalid, and inconsistent data in the air-quality dataset.

Normalisation converts data into a consistent format for accurate analysis.

## 2. Data Cleaning Techniques

### A. Handling Missing Values

Missing values may occur in PM2.5, PM10, NO2, and temperature columns.

Methods:
- Remove records with excessive missing values.
- Use forward fill for consecutive readings.
- Use median values to replace missing numerical measurements.

### B. Handling Invalid Values

Invalid readings include negative pollution values and impossible temperature measurements.

Rules:
- PM2.5 must be between 0 and 999.
- PM10 must be between 0 and 2000.
- NO2 must be between 0 and 1000.
- Temperature must be between -50°C and 60°C.

Invalid measurements are treated as missing values.

### C. Duplicate Removal

Duplicate records are identified using station, date, and hour.

Only the first occurrence is retained.

### D. Temperature Conversion

Temperature readings recorded in Fahrenheit are converted into Celsius.

Formula:

\[
C = (F-32)\times\frac{5}{9}
\]

## 3. Data Normalisation

### A. Min-Max Normalisation

Min-max normalisation scales numerical values between 0 and 1.

\[
X'=\frac{X-X_{\min}}{X_{\max}-X_{\min}}
\]

### B. Z-Score Normalisation

Z-score normalisation standardises values using the mean and standard deviation.

\[
Z=\frac{X-\mu}{\sigma}
\]

## 4. Alternative Approach

An alternative approach is to remove every record containing a missing value instead of using forward fill or median replacement.

**Advantage:** Simple implementation.

**Disadvantage:** Valuable readings may be lost, reducing the size of the dataset.

## 5. Complexity Analysis

| Operation | Time Complexity |
|---|---|
| Missing-value detection | O(n) |
| Duplicate detection using a set | O(n) average |
| Min-max normalisation | O(n) |
| Z-score normalisation | O(n) |

Here, n represents the number of records.

## 6. Conclusion

Data cleaning and normalisation improve data quality and consistency. Handling missing values, removing duplicates, validating measurements, and converting temperature units help produce reliable air-quality analysis results.
## 7. Pseudocode – Data Cleaning and Normalisation

```text
ALGORITHM Clean_Air_Quality_Data(dataset)

BEGIN
    REMOVE duplicate records

    FOR each record IN dataset DO

        IF any required value is missing THEN
            HANDLE missing value using forward fill
            IF value is still missing THEN
                REPLACE with median value
            END IF
        END IF

        IF temperature unit is Fahrenheit THEN
            temperature ← (temperature - 32) × 5 / 9
        END IF

        IF any measurement is outside valid limits THEN
            MARK value as invalid
            REPLACE invalid value using forward fill or median
        END IF

        ROUND numeric values to 2 decimal places

    END FOR

    SAVE cleaned dataset
    RETURN cleaned dataset
END
```

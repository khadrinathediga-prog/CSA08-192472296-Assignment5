# A4 – Debugging and Profiling

## 1. Introduction

Debugging identifies and fixes errors in a program. Profiling measures program performance and identifies time-consuming operations.

Both techniques improve the reliability and efficiency of the air-quality monitoring system.

## 2. Debugging Techniques

### A. Print Statements

Print statements display variable values and program execution details.

```python
print("Current PM2.5:", pm25)
```

### B. Assertions

Assertions check whether expected conditions are satisfied.

```python
assert pm25 >= 0, "Invalid PM2.5 reading"
```

### C. Logging

Logging records program events, warnings, and errors.

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Data processing started")
logging.warning("Missing air-quality value detected")
```

### D. Python Debugger

The `pdb` module allows step-by-step program execution and inspection of variables.

```python
import pdb

pdb.set_trace()
```

## 3. Profiling Techniques

### A. time.perf_counter()

Measures the execution time of a program.

```python
import time

start = time.perf_counter()

# Execute program

end = time.perf_counter()

print("Execution time:", end - start)
```

### B. timeit

Measures the execution time of small code sections.

```python
import timeit

execution_time = timeit.timeit(
    "sum(range(1000))",
    number=1000
)

print("Execution time:", execution_time)
```

### C. cProfile

Identifies functions that consume significant execution time.

```python
import cProfile

cProfile.run("sum(range(100000))")
```

## 4. Alternative Approach

Using only print statements is a simple debugging approach.

**Advantages:**
- Easy to implement.
- Useful for checking variable values.

**Disadvantages:**
- Can produce excessive output.
- Does not provide detailed performance information.
- Requires manual inspection.

Using logging and profiling tools provides better debugging and performance analysis.

## 5. Complexity Analysis

| Technique | Purpose |
|---|---|
| Print statements | Inspect variable values |
| Assertions | Validate conditions |
| Logging | Record events and errors |
| pdb | Step-by-step debugging |
| time.perf_counter() | Measure execution time |
| timeit | Benchmark code sections |
| cProfile | Analyse function performance |

## 6. Conclusion

Debugging and profiling improve program correctness and performance. Python provides built-in tools such as pdb, logging, timeit, and cProfile to identify errors and performance bottlenecks in the air-quality monitoring system.
## 7. Pseudocode – Debugging and Profiling

```text
ALGORITHM Debug_And_Profile(program)

BEGIN
    SET debugging flag to TRUE

    IF debugging flag is TRUE THEN
        DISPLAY relevant variable values
        CHECK input and output values using assertions
        RECORD errors using logging
        USE debugger to inspect program execution
    END IF

    START performance timer

    EXECUTE program

    STOP performance timer

    CALCULATE execution time

    USE profiler to identify time-consuming functions

    DISPLAY execution time and profiling results

    IF errors are found THEN
        FIX errors
        TEST program again
    END IF

    RETURN tested program
END
```
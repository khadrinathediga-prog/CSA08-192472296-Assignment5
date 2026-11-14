
import cProfile
import pstats
import io
from pathlib import Path

from performance_comparison import python_csv_analysis

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "input" / "air_quality_120_stations.csv"

def run_profiling():
    profiler = cProfile.Profile()

    profiler.enable()
    result = python_csv_analysis(DATA_FILE)
    profiler.disable()

    output = io.StringIO()

    stats = pstats.Stats(profiler, stream=output)
    stats.sort_stats("cumulative")
    stats.print_stats(15)

    print("C-PROFILE PERFORMANCE REPORT")
    print("=" * 50)
    print(output.getvalue())

    print("Stations analysed:", len(result))
    print("Profiling completed successfully!")


if __name__ == "__main__":
    run_profiling()

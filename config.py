from pathlib import Path

# Root folder of the project
BASE_DIR = Path(__file__).resolve().parent

# Data folders
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Specific data sources
ALGOTEST_DIR = RAW_DATA_DIR / "algotest"
STOCKMOCK_DIR = RAW_DATA_DIR / "stockmock"
NSE_DIR = RAW_DATA_DIR / "nse"
VIX_DIR = RAW_DATA_DIR / "vix"

# Output folders
REPORTS_DIR = BASE_DIR / "reports"
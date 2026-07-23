from pathlib import Path

# Project Root Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data Paths
RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "city_day.csv"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed"

# Model Path
MODEL_PATH = BASE_DIR / "models"

# Reports Path
REPORT_PATH = BASE_DIR / "reports"
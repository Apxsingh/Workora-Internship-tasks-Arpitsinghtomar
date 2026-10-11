
from pathlib import Path
import pandas as pd

# Folder containing this Python script
PROJECT_DIR = Path(__file__).resolve().parent

# Folder containing the CSV files
DATA_DIR = PROJECT_DIR / "data"

# CSV files to inspect
csv_files = [
    "web_traffic.csv",
    "customer_churn.csv",
    "checkout_ab_test.csv",
    "regional_market.csv",
]

for filename in csv_files:
    file_path = DATA_DIR / filename

    print("\n" + "=" * 70)
    print(f"DATASET: {filename}")
    print("=" * 70)

    if not file_path.is_file():
        print(f"File not found: {file_path}")
        continue

    try:
        df = pd.read_csv(file_path)

        print("Dataset loaded successfully!")
        print("Shape (rows, columns):", df.shape)

        print("\nColumn names:")
        print(df.columns.tolist())

        print("\nFirst 5 rows:")
        print(df.head())

        print("\nMissing values per column:")
        print(df.isnull().sum())

        print("\nDuplicate rows:", df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {filename}: {e}")
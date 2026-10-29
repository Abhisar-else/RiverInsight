"""Lightweight CSV inventory for Phase 1/2. Does not upload or modify data."""
from pathlib import Path
import pandas as pd


def audit_csv(path: str | Path) -> dict:
    """Return basic shape, columns, missingness, and duplicate-row information."""
    path = Path(path)
    df = pd.read_csv(path, nrows=100_000)
    return {
        "file": str(path),
        "rows_inspected": len(df),
        "columns": list(df.columns),
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "missing_count": df.isna().sum().to_dict(),
        "missing_percent": (df.isna().mean() * 100).round(2).to_dict(),
        "duplicate_rows_in_sample": int(df.duplicated().sum()),
    }


if __name__ == "__main__":
    import argparse
    import json
    parser = argparse.ArgumentParser(description="Inspect a CSV without loading more than 100,000 rows.")
    parser.add_argument("csv_path")
    args = parser.parse_args()
    print(json.dumps(audit_csv(args.csv_path), indent=2, default=str))

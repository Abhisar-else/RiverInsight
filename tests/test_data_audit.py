from pathlib import Path
import pandas as pd
from src.data_audit import audit_csv


def test_audit_csv_reports_missing_values(tmp_path: Path):
    csv_path = tmp_path / "sample.csv"
    pd.DataFrame({"x": [1, None, 3], "y": ["a", "b", "c"]}).to_csv(csv_path, index=False)
    result = audit_csv(csv_path)
    assert result["rows_inspected"] == 3
    assert result["missing_count"]["x"] == 1
    assert result["duplicate_rows_in_sample"] == 0

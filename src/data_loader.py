"""Load GeoPulse worksheets from the cleaned Excel workbook."""
from pathlib import Path
import pandas as pd

from config import (
    DEFAULT_WORKBOOK, BUSINESSES_SHEET, MOBILITY_SHEET, PEDESTRIAN_SHEET,
    DQ_SUMMARY_SHEET, FIELD_QUALITY_SHEET, DQ_FINDINGS_SHEET,
)

def load_sheet(sheet_name: str, workbook_path=DEFAULT_WORKBOOK) -> pd.DataFrame:
    """Load one worksheet; raise a clear error if the file or sheet is absent."""
    path = Path(workbook_path)
    if not path.exists():
        raise FileNotFoundError(
            f"Workbook not found: {path}. Place it in the project's data/ folder "
            "or pass workbook_path explicitly."
        )
    try:
        return pd.read_excel(path, sheet_name=sheet_name)
    except ValueError as exc:
        raise ValueError(f"Worksheet '{sheet_name}' was not found in {path.name}.") from exc

def load_businesses(workbook_path=DEFAULT_WORKBOOK):
    return load_sheet(BUSINESSES_SHEET, workbook_path)

def load_mobility(workbook_path=DEFAULT_WORKBOOK):
    return load_sheet(MOBILITY_SHEET, workbook_path)

def load_pedestrian_counts(workbook_path=DEFAULT_WORKBOOK):
    return load_sheet(PEDESTRIAN_SHEET, workbook_path)

def load_data_quality_sheets(workbook_path=DEFAULT_WORKBOOK) -> dict:
    """Load the three workbook sheets documenting data quality."""
    return {
        "summary": load_sheet(DQ_SUMMARY_SHEET, workbook_path),
        "field_quality": load_sheet(FIELD_QUALITY_SHEET, workbook_path),
        "findings": load_sheet(DQ_FINDINGS_SHEET, workbook_path),
    }

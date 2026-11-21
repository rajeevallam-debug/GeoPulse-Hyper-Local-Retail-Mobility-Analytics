"""Shared configuration for GeoPulse source modules."""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
DEFAULT_WORKBOOK = DATA_DIR / "GeoPulse_Cleaned_Data_Quality_FIXED.xlsx"

BUSINESSES_SHEET = "Businesses_dataset_20261111"
MOBILITY_SHEET = "smart_mobility_dataset"
PEDESTRIAN_SHEET = "Bi-Annual_Pedestrian_Counts_202"
DQ_SUMMARY_SHEET = "DQ_Summary"
FIELD_QUALITY_SHEET = "Field_Quality"
DQ_FINDINGS_SHEET = "DQ_Findings"

LATITUDE = "Latitude"
LONGITUDE = "Longitude"

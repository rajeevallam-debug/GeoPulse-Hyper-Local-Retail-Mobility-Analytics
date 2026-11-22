"""Reusable quality checks for GeoPulse tables."""
import pandas as pd

BUSINESS_REQUIRED = ["Business Name", "Latitude", "Longitude"]
MOBILITY_REQUIRED = [
    "Timestamp", "Latitude", "Longitude", "Vehicle_Count",
    "Traffic_Speed_kmh", "Road_Occupancy_%", "Traffic_Condition",
]
PEDESTRIAN_REQUIRED = ["Borough", "Street_Nam"]

def missing_columns(df: pd.DataFrame, required_columns) -> list:
    return [column for column in required_columns if column not in df.columns]

def validate_required_columns(df: pd.DataFrame, required_columns) -> dict:
    missing = missing_columns(df, required_columns)
    return {"valid": not missing, "missing_columns": missing}

def quality_report(df: pd.DataFrame) -> dict:
    """Summarise row count, duplicate rows, missing cells, and column types."""
    return {
        "row_count": int(len(df)),
        "column_count": int(len(df.columns)),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_cells": int(df.isna().sum().sum()),
        "missing_by_column": df.isna().sum().astype(int).to_dict(),
        "data_types": df.dtypes.astype(str).to_dict(),
    }

def validate_coordinates(df: pd.DataFrame, latitude="Latitude", longitude="Longitude") -> pd.Series:
    """Return a row-wise validity mask; invalid/missing values return False."""
    absent = {latitude, longitude}.difference(df.columns)
    if absent:
        raise KeyError(f"Missing coordinate columns: {sorted(absent)}")
    lat = pd.to_numeric(df[latitude], errors="coerce")
    lon = pd.to_numeric(df[longitude], errors="coerce")
    return lat.between(-90, 90) & lon.between(-180, 180)

def validate_mobility_ranges(df: pd.DataFrame) -> pd.DataFrame:
    """Return a table of basic range checks without modifying source records."""
    checks = []
    rules = {
        "Latitude": (-90, 90),
        "Longitude": (-180, 180),
        "Road_Occupancy_%": (0, 100),
    }
    for column, (low, high) in rules.items():
        if column in df.columns:
            values = pd.to_numeric(df[column], errors="coerce")
            checks.append({
                "column": column,
                "minimum_allowed": low,
                "maximum_allowed": high,
                "out_of_range_count": int((~values.between(low, high) & values.notna()).sum()),
                "missing_or_non_numeric_count": int(values.isna().sum()),
            })
    return pd.DataFrame(checks)

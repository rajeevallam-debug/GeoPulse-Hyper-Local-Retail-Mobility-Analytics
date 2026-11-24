"""Location-oriented helpers for business and mobility data."""
import pandas as pd
from data_validation import validate_coordinates

def valid_location_rows(df: pd.DataFrame, latitude="Latitude", longitude="Longitude"):
    """Return a copy containing rows with valid latitude/longitude values."""
    mask = validate_coordinates(df, latitude, longitude)
    result = df.loc[mask].copy()
    result[latitude] = pd.to_numeric(result[latitude], errors="coerce")
    result[longitude] = pd.to_numeric(result[longitude], errors="coerce")
    return result

def counts_by_area(df: pd.DataFrame, area_column="Borough") -> pd.DataFrame:
    """Count records by an available administrative/geographic area field."""
    if area_column not in df.columns:
        raise KeyError(f"Area column '{area_column}' is missing.")
    return (
        df.groupby(area_column, dropna=False)
          .size().rename("record_count")
          .reset_index()
          .sort_values("record_count", ascending=False)
    )

def average_metric_by_area(df: pd.DataFrame, metric: str, area_column="Borough"):
    """Calculate the mean of a numeric metric grouped by area."""
    required = {metric, area_column}.difference(df.columns)
    if required:
        raise KeyError(f"Missing columns: {sorted(required)}")
    data = df[[area_column, metric]].copy()
    data[metric] = pd.to_numeric(data[metric], errors="coerce")
    return data.groupby(area_column, dropna=False)[metric].mean().reset_index()

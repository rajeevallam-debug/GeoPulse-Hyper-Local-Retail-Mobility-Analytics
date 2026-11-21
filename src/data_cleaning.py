"""Explicit, conservative cleaning helpers for GeoPulse datasets."""
import pandas as pd

def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with trimmed column labels; preserve original wording otherwise."""
    result = df.copy()
    result.columns = [c.strip() if isinstance(c, str) else c for c in result.columns]
    return result

def remove_exact_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove fully identical rows only. No business-key assumptions are made."""
    return df.drop_duplicates().copy()

def convert_mobility_timestamp(df: pd.DataFrame, column="Timestamp") -> pd.DataFrame:
    """Convert the mobility timestamp to datetime; invalid values become NaT."""
    result = df.copy()
    if column not in result.columns:
        raise KeyError(f"Required timestamp column '{column}' is missing.")
    result[column] = pd.to_datetime(result[column], errors="coerce")
    return result

def clean_business_coordinates(df: pd.DataFrame) -> pd.DataFrame:
    """Convert coordinate fields to numeric and flag invalid coordinate rows.

    Rows are retained. A Boolean 'coordinates_valid' field is added so the
    analyst can decide whether exclusion is appropriate for a particular task.
    """
    result = df.copy()
    required = {"Latitude", "Longitude"}
    missing = required.difference(result.columns)
    if missing:
        raise KeyError(f"Missing coordinate columns: {sorted(missing)}")
    result["Latitude"] = pd.to_numeric(result["Latitude"], errors="coerce")
    result["Longitude"] = pd.to_numeric(result["Longitude"], errors="coerce")
    result["coordinates_valid"] = (
        result["Latitude"].between(-90, 90)
        & result["Longitude"].between(-180, 180)
    )
    return result

def clean_mobility_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply safe type conversion and duplicate removal to mobility records."""
    result = standardize_column_names(df)
    result = convert_mobility_timestamp(result)
    return remove_exact_duplicates(result)

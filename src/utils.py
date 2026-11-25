"""Small shared helpers used across GeoPulse source modules."""
from pathlib import Path
import pandas as pd

def ensure_directory(path) -> Path:
    """Create a directory (including parents) and return its Path."""
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory

def save_dataframe(df: pd.DataFrame, path, index=False) -> Path:
    """Save a DataFrame as CSV or Excel based on the file extension."""
    destination = Path(path)
    ensure_directory(destination.parent)
    suffix = destination.suffix.lower()
    if suffix == ".csv":
        df.to_csv(destination, index=index)
    elif suffix in {".xlsx", ".xls"}:
        df.to_excel(destination, index=index)
    else:
        raise ValueError("Supported output formats are .csv, .xlsx, and .xls")
    return destination

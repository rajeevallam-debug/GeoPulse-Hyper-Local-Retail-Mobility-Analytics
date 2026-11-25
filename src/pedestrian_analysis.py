"""Analysis helpers for the wide-format pedestrian count worksheet."""
import re
import pandas as pd

ID_COLUMNS = [
    "the_geom", "OBJECTID", "Loc", "Borough", "Street_Nam",
    "From_Stree", "To_Street", "Iex",
]

def pedestrian_measurement_columns(df: pd.DataFrame) -> list:
    """Find survey columns such as May07_AM, Oct24_PM, or May26_MD."""
    pattern = re.compile(r"^(May|Sept|Oct|June)\d{2}_(AM|PM|MD)$")
    return [c for c in df.columns if isinstance(c, str) and pattern.match(c)]

def to_long_format(df: pd.DataFrame) -> pd.DataFrame:
    """Reshape survey-period columns into one row per location and period."""
    value_columns = pedestrian_measurement_columns(df)
    if not value_columns:
        raise ValueError("No recognised pedestrian survey columns were found.")
    id_columns = [c for c in ID_COLUMNS if c in df.columns]
    long_df = df.melt(
        id_vars=id_columns,
        value_vars=value_columns,
        var_name="survey_period",
        value_name="pedestrian_count",
    )
    long_df["pedestrian_count"] = pd.to_numeric(
        long_df["pedestrian_count"], errors="coerce"
    )
    parts = long_df["survey_period"].str.extract(
        r"^(?P<survey_month_year>.+)_(?P<time_period>AM|PM|MD)$"
    )
    long_df = pd.concat([long_df, parts], axis=1)
    return long_df

def average_count_by_borough(df: pd.DataFrame) -> pd.DataFrame:
    if "Borough" not in df.columns:
        raise KeyError("Missing 'Borough' column.")
    long_df = to_long_format(df)
    return long_df.groupby("Borough", dropna=False)["pedestrian_count"].mean().reset_index(
        name="average_pedestrian_count"
    )

def average_count_by_time_period(df: pd.DataFrame) -> pd.DataFrame:
    long_df = to_long_format(df)
    return long_df.groupby("time_period", dropna=False)["pedestrian_count"].mean().reset_index(
        name="average_pedestrian_count"
    )

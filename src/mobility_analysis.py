"""Analysis functions for the smart_mobility_dataset worksheet."""
import pandas as pd

def prepare_mobility(df: pd.DataFrame) -> pd.DataFrame:
    """Copy data and parse Timestamp; source DataFrame remains unchanged."""
    if "Timestamp" not in df.columns:
        raise KeyError("The mobility data must contain 'Timestamp'.")
    result = df.copy()
    result["Timestamp"] = pd.to_datetime(result["Timestamp"], errors="coerce")
    return result

def traffic_condition_counts(df: pd.DataFrame) -> pd.DataFrame:
    if "Traffic_Condition" not in df.columns:
        raise KeyError("Missing 'Traffic_Condition' column.")
    return df["Traffic_Condition"].value_counts(dropna=False).rename_axis(
        "Traffic_Condition"
    ).reset_index(name="record_count")

def hourly_traffic_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Summarise vehicle count and speed by hour of day."""
    data = prepare_mobility(df)
    for column in ["Vehicle_Count", "Traffic_Speed_kmh"]:
        if column not in data.columns:
            raise KeyError(f"Missing '{column}' column.")
        data[column] = pd.to_numeric(data[column], errors="coerce")
    data = data.dropna(subset=["Timestamp"])
    data["hour"] = data["Timestamp"].dt.hour
    return data.groupby("hour").agg(
        average_vehicle_count=("Vehicle_Count", "mean"),
        average_speed_kmh=("Traffic_Speed_kmh", "mean"),
        observations=("Timestamp", "size"),
    ).reset_index()

def average_metrics_by_condition(df: pd.DataFrame) -> pd.DataFrame:
    metrics = [
        "Vehicle_Count", "Traffic_Speed_kmh", "Road_Occupancy_%",
        "Emission_Levels_g_km", "Energy_Consumption_L_h",
    ]
    if "Traffic_Condition" not in df.columns:
        raise KeyError("Missing 'Traffic_Condition' column.")
    available = [c for c in metrics if c in df.columns]
    data = df[["Traffic_Condition"] + available].copy()
    for column in available:
        data[column] = pd.to_numeric(data[column], errors="coerce")
    return data.groupby("Traffic_Condition", dropna=False)[available].mean().reset_index()

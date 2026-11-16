import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_raw_dataset(filepath: str, num_records: int = 2500) -> None:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    np.random.seed(42)

    zones = {
        "Electronic City": (12.8452, 77.6602),
        "Koramangala": (12.9352, 77.6245),
        "Indiranagar": (12.9784, 77.6408),
        "Whitefield": (12.9698, 77.7500),
        "Jayanagar": (12.9308, 77.5838)
    }
    categories = ["Supermarket", "Cafe & QSR", "Apparel", "Electronics", "Pharmacy"]
    store_ids = [f"STR_{i:03d}" for i in range(101, 131)]

    zone_choices = np.random.choice(list(zones.keys()), size=num_records, p=[0.25, 0.25, 0.20, 0.18, 0.12])
    lats = [zones[z][0] + np.random.normal(0, 0.008) for z in zone_choices]
    lons = [zones[z][1] + np.random.normal(0, 0.008) for z in zone_choices]

    base_time = datetime(2026, 10, 1, 8, 0, 0)
    timestamps = [
        base_time + timedelta(days=int(np.random.randint(0, 30)), hours=int(np.random.choice(range(8, 22))), minutes=int(np.random.randint(0, 60)))
        for _ in range(num_records)
    ]

    df = pd.DataFrame({
        "visit_id": [f"VST_{10000 + i}" for i in range(num_records)],
        "user_device_hash": [f"DEV_{np.random.randint(1000, 1850)}" for _ in range(num_records)],
        "store_id": np.random.choice(store_ids, size=num_records),
        "store_category": np.random.choice(categories, size=num_records, p=[0.30, 0.25, 0.20, 0.10, 0.15]),
        "zone_name": zone_choices,
        "latitude": np.round(lats, 6),
        "longitude": np.round(lons, 6),
        "visit_timestamp": timestamps,
        "dwell_time_mins": np.random.gamma(shape=2.5, scale=10.0, size=num_records).astype(int) + 3,
        "transaction_amount_inr": np.round(np.random.lognormal(mean=6.2, sigma=0.75, size=num_records), 2)
    })

    df.loc[np.random.choice(df.index, 25, replace=False), "dwell_time_mins"] = np.nan
    df = pd.concat([df, df.iloc[:15]], ignore_index=True)
    df.to_csv(filepath, index=False)
    print(f"[ETL] Generated raw dataset: {filepath} ({len(df)} rows)")

def run_etl_pipeline(raw_path: str, cleaned_path: str) -> pd.DataFrame:
    if not os.path.exists(raw_path):
        generate_raw_dataset(raw_path)

    df = pd.read_csv(raw_path)
    initial_rows = len(df)

    df = df.drop_duplicates(subset=["visit_id"]).copy()
    df = df.dropna(subset=["visit_id", "store_id", "zone_name", "latitude", "longitude", "visit_timestamp"])

    median_dwell = df["dwell_time_mins"].median()
    df["dwell_time_mins"] = df["dwell_time_mins"].fillna(median_dwell).astype(int)

    df = df[(df["latitude"].between(12.70, 13.20)) & (df["longitude"].between(77.30, 77.90))]
    df = df[df["dwell_time_mins"] > 0]

    df["visit_timestamp"] = pd.to_datetime(df["visit_timestamp"])
    df["visit_date"] = df["visit_timestamp"].dt.date.astype(str)
    df["hour_of_day"] = df["visit_timestamp"].dt.hour
    df["day_of_week"] = df["visit_timestamp"].dt.day_name()
    df["is_weekend"] = df["day_of_week"].isin(["Saturday", "Sunday"]).astype(int)
    df["time_slot"] = pd.cut(
        df["hour_of_day"],
        bins=[0, 11, 16, 20, 24],
        labels=["Morning (8-11)", "Afternoon (12-16)", "Evening (17-20)", "Night (21+)"],
        right=True
    ).astype(str)

    os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)
    df.to_csv(cleaned_path, index=False)
    print(f"[ETL] Cleaned data saved to {cleaned_path} ({len(df)} valid rows, {initial_rows - len(df)} removed)")
    return df

if __name__ == "__main__":
    run_etl_pipeline("data/raw_retail_mobility.csv", "outputs/cleaned_retail_mobility.csv")

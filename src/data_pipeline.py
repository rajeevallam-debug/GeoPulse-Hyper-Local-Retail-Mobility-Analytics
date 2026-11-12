import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_sample_mobility_data(num_records=1000) -> pd.DataFrame:
    """Generates synthetic retail mobility data for GeoPulse testing."""
    np.random.seed(42)
    
    store_categories = ['Supermarket', 'Apparel', 'Electronics', 'Cafe', 'Pharmacy']
    zones = ['Zone_A_Downtown', 'Zone_B_Suburbs', 'Zone_C_Mall', 'Zone_D_HighStreet']
    
    start_date = datetime(2026, 11, 1)
    timestamps = [start_date + timedelta(hours=int(np.random.randint(0, 720))) for _ in range(num_records)]
    
    data = {
        'visit_id': [f"VST_{1000 + i}" for i in range(num_records)],
        'store_id': [f"STR_{np.random.randint(101, 120)}" for _ in range(num_records)],
        'store_category': np.random.choice(store_categories, num_records),
        'zone_id': np.random.choice(zones, num_records),
        'latitude': np.round(np.random.uniform(12.9000, 13.0000, num_records), 6),
        'longitude': np.round(np.random.uniform(77.5000, 77.6500, num_records), 6),
        'visit_timestamp': timestamps,
        'dwell_time_minutes': np.random.exponential(scale=25, size=num_records).astype(int) + 5,
        'spend_amount': np.round(np.random.gamma(shape=2, scale=500, size=num_records), 2)
    }
    
    return pd.DataFrame(data)

def clean_and_validate_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans mobility logs by dropping duplicates, handling nulls, and extracting time features."""
    initial_count = len(df)
    
    # Drop duplicates
    df = df.drop_duplicates(subset=['visit_id'])
    
    # Handle missing values in critical columns
    df = df.dropna(subset=['store_id', 'latitude', 'longitude', 'visit_timestamp'])
    
    # Feature Engineering from Timestamps
    df['visit_timestamp'] = pd.to_datetime(df['visit_timestamp'])
    df['hour_of_day'] = df['visit_timestamp'].dt.hour
    df['day_of_week'] = df['visit_timestamp'].dt.day_name()
    df['is_weekend'] = df['day_of_week'].isin(['Saturday', 'Sunday'])
    
    print(f"Data Cleaned Successfully. Processed {len(df)} valid records out of {initial_count}.")
    return df

if __name__ == "__main__":
    raw_df = generate_sample_mobility_data(1500)
    cleaned_df = clean_and_validate_data(raw_df)
    cleaned_df.to_csv("data/cleaned_geopulse_mobility.csv", index=False)
    print("Exported cleaned dataset to data/cleaned_geopulse_mobility.csv")

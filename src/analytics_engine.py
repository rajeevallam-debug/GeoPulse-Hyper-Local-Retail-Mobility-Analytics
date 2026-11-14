import pandas as pd

def compute_key_metrics(csv_filepath: str):
    """Computes spatial and temporal retail insights for GeoPulse."""
    df = pd.read_csv(csv_filepath)
    
    print("--- GEO-PULSE ANALYTICAL INSIGHTS REPORT ---")
    
    # 1. Total Visits and Revenue by Zone
    zone_summary = df.groupby('zone_id').agg(
        total_visits=('visit_id', 'count'),
        avg_dwell_time=('dwell_time_minutes', 'mean'),
        total_revenue=('spend_amount', 'sum')
    ).reset_index().sort_values(by='total_visits', ascending=False)
    
    print("\n[1] Performance Summary by Retail Zone:")
    print(zone_summary.to_string(index=False))
    
    # 2. Peak Footfall Hours
    peak_hours = df.groupby('hour_of_day')['visit_id'].count().reset_index(name='footfall_count')
    peak_hour = peak_hours.loc[peak_hours['footfall_count'].idxmax()]
    print(f"\n[2] Peak Footfall Hour across all zones: {int(peak_hour['hour_of_day'])}:00 ({int(peak_hour['footfall_count'])} visits)")

    # 3. Category Breakdown
    category_summary = df.groupby('store_category').agg(
        total_visits=('visit_id', 'count'),
        avg_spend=('spend_amount', 'mean')
    ).reset_index()
    
    print("\n[3] Category Performance Breakdown:")
    print(category_summary.to_string(index=False))

if __name__ == "__main__":
    try:
        compute_key_metrics("data/cleaned_geopulse_mobility.csv")
    except FileNotFoundError:
        print("Cleaned data file not found. Please run data_pipeline.py first.")

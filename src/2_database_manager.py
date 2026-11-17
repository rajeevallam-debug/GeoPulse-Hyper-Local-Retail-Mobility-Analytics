import os
import sqlite3
import pandas as pd

def build_database_and_query(cleaned_csv_path: str, db_path: str) -> dict:
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    df = pd.read_csv(cleaned_csv_path)

    conn = sqlite3.connect(db_path)
    df.to_sql("retail_mobility", conn, if_exists="replace", index=False)

    queries = {
        "zone_performance": """
            SELECT 
                zone_name,
                COUNT(visit_id) AS total_footfall,
                COUNT(DISTINCT user_device_hash) AS unique_visitors,
                ROUND(AVG(dwell_time_mins), 2) AS avg_dwell_mins,
                ROUND(SUM(transaction_amount_inr), 2) AS total_revenue_inr,
                ROUND(AVG(transaction_amount_inr), 2) AS avg_ticket_size_inr
            FROM retail_mobility
            GROUP BY zone_name
            ORDER BY total_revenue_inr DESC;
        """,
        "hourly_footfall_trends": """
            SELECT 
                hour_of_day,
                time_slot,
                COUNT(visit_id) AS visit_count,
                ROUND(SUM(transaction_amount_inr), 2) AS hourly_revenue_inr
            FROM retail_mobility
            GROUP BY hour_of_day, time_slot
            ORDER BY hour_of_day ASC;
        """,
        "category_weekend_split": """
            SELECT 
                store_category,
                CASE WHEN is_weekend = 1 THEN 'Weekend' ELSE 'Weekday' END AS day_type,
                COUNT(visit_id) AS visits,
                ROUND(AVG(dwell_time_mins), 1) AS avg_dwell_mins,
                ROUND(SUM(transaction_amount_inr), 2) AS revenue_inr
            FROM retail_mobility
            GROUP BY store_category, is_weekend
            ORDER BY store_category, day_type;
        """,
        "top_stores": """
            SELECT 
                store_id,
                zone_name,
                store_category,
                COUNT(visit_id) AS total_visits,
                ROUND(SUM(transaction_amount_inr), 2) AS total_revenue_inr
            FROM retail_mobility
            GROUP BY store_id, zone_name, store_category
            ORDER BY total_revenue_inr DESC
            LIMIT 10;
        """
    }

    results = {}
    for name, sql in queries.items():
        res_df = pd.read_sql_query(sql, conn)
        results[name] = res_df
        res_df.to_csv(f"outputs/sql_{name}.csv", index=False)

    conn.close()
    print(f"[SQL] Database built at {db_path} and 4 analytical tables exported to outputs/")
    return results

if __name__ == "__main__":
    build_database_and_query("outputs/cleaned_retail_mobility.csv", "outputs/geopulse.db")

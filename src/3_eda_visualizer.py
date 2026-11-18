import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_visualizations(sql_results: dict, chart_dir: str) -> None:
    os.makedirs(chart_dir, exist_ok=True)
    sns.set_theme(style="whitegrid")

    # 1. Zone Revenue & Footfall Comparison
    zone_df = sql_results["zone_performance"]
    fig, ax1 = plt.subplots(figsize=(10, 5))
    sns.barplot(data=zone_df, x="zone_name", y="total_revenue_inr", palette="Blues_d", ax=ax1)
    ax1.set_title("Hyper-Local Retail Revenue & Footfall by Zone", fontsize=13, fontweight="bold")
    ax1.set_xlabel("Retail Zone")
    ax1.set_ylabel("Total Revenue (INR)")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(os.path.join(chart_dir, "1_zone_revenue.png"), dpi=300)
    plt.close()

    # 2. Hourly Footfall Mobility Curve
    hourly_df = sql_results["hourly_footfall_trends"]
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=hourly_df, x="hour_of_day", y="visit_count", marker="o", linewidth=2.5, color="#1f77b4")
    plt.title("Hourly Retail Mobility & Peak Footfall Curve", fontsize=13, fontweight="bold")
    plt.xlabel("Hour of Day (24-Hour Format)")
    plt.ylabel("Total Store Visits")
    plt.xticks(range(8, 22))
    plt.tight_layout()
    plt.savefig(os.path.join(chart_dir, "2_hourly_mobility_curve.png"), dpi=300)
    plt.close()

    # 3. Weekday vs Weekend Revenue by Category
    cat_df = sql_results["category_weekend_split"]
    plt.figure(figsize=(10, 5))
    sns.barplot(data=cat_df, x="store_category", y="revenue_inr", hue="day_type", palette="Set2")
    plt.title("Weekday vs. Weekend Revenue Performance by Store Category", fontsize=13, fontweight="bold")
    plt.xlabel("Store Category")
    plt.ylabel("Revenue (INR)")
    plt.legend(title="Period")
    plt.tight_layout()
    plt.savefig(os.path.join(chart_dir, "3_category_weekend_split.png"), dpi=300)
    plt.close()

    print(f"[EDA] Exported 3 analytical charts to {chart_dir}/")

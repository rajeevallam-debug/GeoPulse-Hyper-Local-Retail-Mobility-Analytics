from importlib import import_module

etl = import_module("1_etl_pipeline")
db = import_module("2_database_manager")
viz = import_module("3_eda_visualizer")

def main():
    print("=== Starting GeoPulse Analytics Pipeline ===")
    raw_file = "data/raw_retail_mobility.csv"
    cleaned_file = "outputs/cleaned_retail_mobility.csv"
    db_file = "outputs/geopulse.db"
    charts_folder = "outputs/charts"

    etl.run_etl_pipeline(raw_file, cleaned_file)
    sql_outputs = db.build_database_and_query(cleaned_file, db_file)
    viz.generate_visualizations(sql_outputs, charts_folder)

    print("\n=== Top Performing Zones Summary ===")
    print(sql_outputs["zone_performance"].to_string(index=False))
    print("\n=== Pipeline Completed Successfully ===")

if __name__ == "__main__":
    main()

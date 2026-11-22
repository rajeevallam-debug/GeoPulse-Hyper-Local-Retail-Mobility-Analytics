import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


def run_spatial_clustering(df: pd.DataFrame, n_clusters: int = 5) -> pd.DataFrame:
    coords = df[["latitude", "longitude"]]
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df = df.copy()
    df["hotspot_cluster"] = kmeans.fit_predict(coords)
    return df


def evaluate_spend_models(df: pd.DataFrame, output_path: str) -> pd.DataFrame:
    feature_cols = [
        "store_category",
        "zone_name",
        "hour_of_day",
        "is_weekend",
        "dwell_time_mins",
        "hotspot_cluster",
    ]
    target_col = "transaction_amount_inr"

    model_df = df[feature_cols + [target_col]].dropna().copy()
    categorical_cols = ["store_category", "zone_name"]
    numeric_cols = ["hour_of_day", "is_weekend", "dwell_time_mins", "hotspot_cluster"]

    encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
    encoded_cats = encoder.fit_transform(model_df[categorical_cols])
    encoded_df = pd.DataFrame(
        encoded_cats,
        columns=encoder.get_feature_names_out(categorical_cols),
        index=model_df.index,
    )

    X = pd.concat([model_df[numeric_cols], encoded_df], axis=1)
    y = model_df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
        "LinearRegression": LinearRegression(),
        "RandomForestRegressor": RandomForestRegressor(n_estimators=100, random_state=42),
    }

    metrics_rows = []
    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        metrics_rows.append({
            "model_name": name,
            "mae_inr": round(float(mean_absolute_error(y_test, preds)), 2),
            "rmse_inr": round(float(root_mean_squared_error(y_test, preds)), 2),
            "r2_score": round(float(r2_score(y_test, preds)), 4),
        })

    metrics_df = pd.DataFrame(metrics_rows).sort_values(by="r2_score", ascending=False)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    metrics_df.to_csv(output_path, index=False)
    print(f"[MODEL] Saved evaluation metrics to {output_path}")
    return metrics_df


def run_modeling_pipeline(cleaned_csv_path: str, metrics_output_path: str) -> pd.DataFrame:
    df = pd.read_csv(cleaned_csv_path)
    clustered_df = run_spatial_clustering(df, n_clusters=5)
    clustered_df.to_csv(cleaned_csv_path, index=False)
    return evaluate_spend_models(clustered_df, metrics_output_path)


if __name__ == "__main__":
    summary = run_modeling_pipeline(
        "outputs/cleaned_retail_mobility.csv",
        "outputs/model_evaluation_summary.csv",
    )
    print(summary.to_string(index=False))

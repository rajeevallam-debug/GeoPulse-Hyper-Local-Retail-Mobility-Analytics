-- Missing values in key business fields.
SELECT
    COUNT(*) AS total_rows,
    COUNT(*) FILTER (WHERE business_name IS NULL OR BTRIM(business_name) = '') AS missing_business_name,
    COUNT(*) FILTER (WHERE borough IS NULL OR BTRIM(borough) = '') AS missing_borough,
    COUNT(*) FILTER (WHERE latitude IS NULL) AS missing_latitude,
    COUNT(*) FILTER (WHERE longitude IS NULL) AS missing_longitude
FROM businesses;

-- Coordinate validity checks.
SELECT
    COUNT(*) AS total_rows,
    COUNT(*) FILTER (
        WHERE latitude IS NULL OR longitude IS NULL
           OR latitude NOT BETWEEN -90 AND 90
           OR longitude NOT BETWEEN -180 AND 180
    ) AS invalid_coordinate_rows
FROM businesses;

-- Mobility missingness and duplicate timestamp/location combinations.
SELECT
    COUNT(*) AS total_rows,
    COUNT(*) FILTER (WHERE recorded_at IS NULL) AS missing_timestamp,
    COUNT(*) FILTER (WHERE vehicle_count IS NULL) AS missing_vehicle_count,
    COUNT(*) FILTER (WHERE traffic_speed_kmh IS NULL) AS missing_speed,
    COUNT(*) FILTER (WHERE traffic_condition IS NULL) AS missing_traffic_condition
FROM smart_mobility;

SELECT recorded_at, latitude, longitude, COUNT(*) AS duplicate_count
FROM smart_mobility
GROUP BY recorded_at, latitude, longitude
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;

-- Check plausible numeric ranges without deleting records.
SELECT
    COUNT(*) FILTER (WHERE vehicle_count < 0) AS negative_vehicle_counts,
    COUNT(*) FILTER (WHERE traffic_speed_kmh < 0) AS negative_speeds,
    COUNT(*) FILTER (WHERE road_occupancy_pct NOT BETWEEN 0 AND 100) AS occupancy_out_of_range,
    COUNT(*) FILTER (WHERE sentiment_score NOT BETWEEN -1 AND 1) AS sentiment_out_of_range
FROM smart_mobility;

-- Inspect the workbook's documented quality summaries.
SELECT * FROM dq_summary ORDER BY dataset;
SELECT * FROM dq_findings ORDER BY dataset, issue;

-- Category distributions.
SELECT borough, COUNT(*) AS business_count
FROM businesses
GROUP BY borough
ORDER BY business_count DESC;

SELECT traffic_condition, COUNT(*) AS observation_count
FROM smart_mobility
GROUP BY traffic_condition
ORDER BY observation_count DESC;

SELECT weather_condition, COUNT(*) AS observation_count
FROM smart_mobility
GROUP BY weather_condition
ORDER BY observation_count DESC;

SELECT traffic_light_state, COUNT(*) AS observation_count
FROM smart_mobility
GROUP BY traffic_light_state
ORDER BY observation_count DESC;

-- Numeric ranges and basic descriptive statistics.
SELECT
    MIN(vehicle_count) AS min_vehicle_count,
    AVG(vehicle_count) AS avg_vehicle_count,
    MAX(vehicle_count) AS max_vehicle_count,
    MIN(traffic_speed_kmh) AS min_speed_kmh,
    AVG(traffic_speed_kmh) AS avg_speed_kmh,
    MAX(traffic_speed_kmh) AS max_speed_kmh,
    MIN(road_occupancy_pct) AS min_occupancy_pct,
    AVG(road_occupancy_pct) AS avg_occupancy_pct,
    MAX(road_occupancy_pct) AS max_occupancy_pct
FROM smart_mobility;

-- Pedestrian survey columns available in the imported wide table.
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'pedestrian_counts_wide'
ORDER BY ordinal_position;

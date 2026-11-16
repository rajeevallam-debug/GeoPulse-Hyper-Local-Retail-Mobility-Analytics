-- ==========================================================
-- Project: GeoPulse: Hyper-Local Retail Mobility Analytics
-- Description: SQL Queries for Spatial, Temporal, & Revenue Analysis
-- ==========================================================

-- 1. High-Level Zone Performance Overview
-- Aggregates total footfall, average dwell time, and total spend per retail zone
SELECT 
    zone_id,
    COUNT(visit_id) AS total_visitors,
    ROUND(AVG(dwell_time_minutes), 2) AS avg_dwell_time_mins,
    ROUND(SUM(spend_amount), 2) AS total_zone_revenue,
    ROUND(AVG(spend_amount), 2) AS avg_spend_per_visit
FROM retail_mobility_logs
GROUP BY zone_id
ORDER BY total_zone_revenue DESC;

-- 2. Peak Footfall Hours Identification
-- Identifies busiest hours across store categories to optimize staffing and marketing
SELECT 
    store_category,
    hour_of_day,
    COUNT(visit_id) AS footfall_volume
FROM retail_mobility_logs
GROUP BY store_category, hour_of_day
ORDER BY store_category, footfall_volume DESC;

-- 3. Weekday vs. Weekend Mobility Behavior
-- Compares customer behavior patterns between weekdays and weekends
SELECT 
    zone_id,
    CASE 
        WHEN is_weekend = TRUE THEN 'Weekend'
        ELSE 'Weekday'
    END AS period_type,
    COUNT(visit_id) AS visit_count,
    ROUND(AVG(spend_amount), 2) AS average_spend
FROM retail_mobility_logs
GROUP BY zone_id, is_weekend
ORDER BY zone_id, period_type DESC;

-- 4. Top Performing Stores by Footfall Density
SELECT 
    store_id,
    store_category,
    zone_id,
    COUNT(visit_id) AS total_visits
FROM retail_mobility_logs
GROUP BY store_id, store_category, zone_id
ORDER BY total_visits DESC
LIMIT 10;

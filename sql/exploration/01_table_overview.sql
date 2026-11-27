-- Row counts for the imported GeoPulse tables.
SELECT 'businesses' AS table_name, COUNT(*) AS row_count FROM businesses
UNION ALL
SELECT 'smart_mobility', COUNT(*) FROM smart_mobility
UNION ALL
SELECT 'pedestrian_counts_wide', COUNT(*) FROM pedestrian_counts_wide
UNION ALL
SELECT 'dq_summary', COUNT(*) FROM dq_summary
UNION ALL
SELECT 'field_quality', COUNT(*) FROM field_quality
UNION ALL
SELECT 'dq_findings', COUNT(*) FROM dq_findings
ORDER BY table_name;

-- Preview a few records from each main dataset.
SELECT * FROM businesses LIMIT 10;
SELECT * FROM smart_mobility ORDER BY recorded_at LIMIT 10;
SELECT objectid, loc, borough, street_nam, from_stree, to_street
FROM pedestrian_counts_wide LIMIT 10;

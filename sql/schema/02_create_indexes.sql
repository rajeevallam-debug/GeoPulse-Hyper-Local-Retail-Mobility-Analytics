-- Indexes for common filtering and grouping patterns.
CREATE INDEX IF NOT EXISTS idx_businesses_borough ON businesses (borough);
CREATE INDEX IF NOT EXISTS idx_businesses_city ON businesses (city);
CREATE INDEX IF NOT EXISTS idx_businesses_coordinates ON businesses (latitude, longitude);

CREATE INDEX IF NOT EXISTS idx_mobility_recorded_at ON smart_mobility (recorded_at);
CREATE INDEX IF NOT EXISTS idx_mobility_condition ON smart_mobility (traffic_condition);
CREATE INDEX IF NOT EXISTS idx_mobility_coordinates ON smart_mobility (latitude, longitude);

CREATE INDEX IF NOT EXISTS idx_pedestrian_borough ON pedestrian_counts_wide (borough);
CREATE INDEX IF NOT EXISTS idx_pedestrian_street ON pedestrian_counts_wide (street_nam);

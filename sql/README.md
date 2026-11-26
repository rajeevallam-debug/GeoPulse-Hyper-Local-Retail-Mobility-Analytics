# GeoPulse SQL

This folder contains PostgreSQL SQL scripts tailored to the uploaded
`GeoPulse_Cleaned_Data_Quality_FIXED.xlsx` workbook.

## Folder structure

```text
sql/
├── README.md
├── schema/
│   ├── 01_create_tables.sql
│   └── 02_create_indexes.sql
├── exploration/
│   ├── 01_table_overview.sql
│   ├── 02_data_quality_checks.sql
│   └── 03_value_exploration.sql
├── aggregations/
│   ├── 01_businesses_by_borough.sql
│   ├── 02_mobility_hourly_summary.sql
│   ├── 03_mobility_by_traffic_condition.sql
│   └── 04_pedestrian_long_format_and_summary.sql
└── analytical_queries/
    ├── 01_traffic_congestion_analysis.sql
    ├── 02_speed_and_occupancy_analysis.sql
    ├── 03_emissions_and_energy_analysis.sql
    ├── 04_business_geographic_distribution.sql
    ├── 05_pedestrian_trend_comparison.sql
    └── 06_mobility_data_quality_flags.sql
```

## Database and naming

These scripts use **PostgreSQL** syntax. The SQL table names use lowercase
snake_case. Source Excel worksheet names are mapped as follows:

| Excel worksheet | PostgreSQL table |
|---|---|
| `Businesses_dataset_20261111` | `businesses` |
| `smart_mobility_dataset` | `smart_mobility` |
| `Bi-Annual_Pedestrian_Counts_202` | `pedestrian_counts_wide` |
| `DQ_Summary` | `dq_summary` |
| `Field_Quality` | `field_quality` |
| `DQ_Findings` | `dq_findings` |

The pedestrian worksheet is supplied in wide format: each survey period/time
combination has its own column (for example, `May07_AM`, `Oct24_PM`, `May26_MD`).
The aggregation script creates a normalized view named `pedestrian_counts_long`
from those columns.

## Recommended execution order

1. Create a PostgreSQL database, for example `geopulse`.
2. Run `schema/01_create_tables.sql`.
3. Import the six Excel worksheets into the corresponding tables. Keep the
   column mapping and date/time parsing consistent with the DDL.
4. Run `schema/02_create_indexes.sql`.
5. Run the scripts in `exploration/` to inspect the imported data.
6. Run `aggregations/` to create summary views.
7. Run the required reports from `analytical_queries/`.

## Import notes

- Import each worksheet separately. PostgreSQL does not read `.xlsx` directly;
  use a database import tool or export each worksheet as CSV first.
- Import into the matching columns. For Excel headers containing spaces or
  punctuation, map them to the snake_case columns shown in the DDL.
- `timestamp` should be imported as `TIMESTAMP`; numeric measures as numeric
  types; identifiers and categorical fields as text or integer as appropriate.
- The scripts assume the imported table names and column names in the DDL.
- If your PostgreSQL import tool creates different names, adjust the SQL or
  rename the imported columns before running these queries.
- The scripts do not infer missing values or remove records. They report
  quality issues so that cleaning decisions remain documented.

## Important interpretation notes

- The business dataset describes business locations; it should not be joined
  to mobility observations as if they were the same events unless a justified
  spatial/time matching method is designed.
- Pedestrian survey columns represent periodic counts, not continuous daily
  observations. Avoid treating them as a continuous time series without noting
  the survey intervals.
- Correlation between traffic, weather, accidents, emissions, or sentiment
  does not establish causation.

Processed Data – GeoPulse

1. Overview

The "processed/" directory contains cleaned, validated and analysis-ready datasets generated during the GeoPulse – Hyper-Local Retail Mobility Analytics project.

These datasets are prepared from the original raw datasets through data inspection, quality assessment, cleaning and transformation activities.

The processed datasets serve as the primary inputs for exploratory data analysis, geographic analysis, statistical analysis and Power BI dashboard development.

2. Purpose

The purpose of this directory is to:

- Store cleaned and validated datasets.
- Maintain consistent data formats and structures.
- Improve data quality and analytical reliability.
- Provide standardized inputs for analysis.
- Support Power BI dashboard development.
- Maintain reproducibility and traceability.
- Separate final analytical datasets from original and temporary data.

3. Processed Dataset Categories

3.1 Processed Business Dataset

Directory: "businesses/"

Purpose: Contains business records after the required data cleaning and validation procedures.

Processing activities:

- Identification and assessment of missing values.
- Duplicate record inspection.
- Column name standardization where required.
- Data type validation.
- Geographic coordinate validation.
- ZIP code and administrative field consistency checks.
- Removal or correction of invalid records where justified.

Important attributes:

Attribute| Description
Business Name| Recorded business name
City| Associated city
ZIP Code| Postal area identifier
Borough| Administrative geographic area
Community Board| Community board identifier
Council District| Council district identifier
Census Tract| Census geographic identifier
Latitude| Validated geographic latitude
Longitude| Validated geographic longitude

Analytical applications:

- Business distribution analysis.
- Borough-wise business comparison.
- ZIP-code-level business concentration.
- Geographic business visualization.

3.2 Processed Smart Mobility Dataset

Directory: "mobility/"

Purpose: Contains mobility observations after data quality assessment and preprocessing.

Processing activities:

- Timestamp format standardization.
- Numeric data type validation.
- Missing value assessment.
- Duplicate observation inspection.
- Geographic coordinate validation.
- Traffic speed and vehicle count range checks.
- Standardization of categorical values.
- Verification of measurement units.

Important attributes:

Attribute| Description
Timestamp| Standardized observation date and time
Latitude| Geographic latitude
Longitude| Geographic longitude
Vehicle_Count| Recorded vehicle count
Traffic_Speed_kmh| Traffic speed
Road_Occupancy_%| Road occupancy percentage
Traffic_Light_State| Traffic signal state
Weather_Condition| Weather observation
Accident_Report| Accident-report field
Ride_Sharing_Demand| Ride-sharing demand
Parking_Availability| Parking availability
Emission_Levels_g_km| Recorded emission level
Traffic_Condition| Traffic condition category

Analytical applications:

- Vehicle activity analysis.
- Traffic speed analysis.
- Road occupancy assessment.
- Traffic condition comparison.
- Weather and traffic pattern analysis.
- Mobility trend visualization.

3.3 Processed Pedestrian Counts Dataset

Directory: "pedestrian_counts/"

Purpose: Contains standardized pedestrian count records prepared for historical footfall analysis.

Processing activities:

- Missing value assessment.
- Duplicate record inspection.
- Street and borough field standardization.
- Numeric pedestrian count validation.
- Historical column transformation where appropriate.
- Restructuring of AM, MD and PM observations into a consistent analytical format.

Recommended analytical structure after unpivoting:

Attribute| Description
Borough| Administrative geographic area
Street_Name| Surveyed street
From_Street| Starting street reference
To_Street| Ending street reference
Survey_Period| Historical survey period
Time_Period| AM, MD or PM
Pedestrian_Count| Recorded pedestrian count

Analytical applications:

- Morning, midday and evening comparisons.
- Street-level pedestrian activity analysis.
- Borough-wise pedestrian comparison.
- Historical footfall analysis.
- Identification of streets with higher recorded pedestrian counts.

4. Data Processing Workflow

The processed datasets are generated through the following workflow:

1. Raw Dataset Collection – Obtain original datasets.
2. Data Inspection – Understand dataset structure and attributes.
3. Data Quality Assessment – Identify missing values, duplicates and inconsistencies.
4. Data Cleaning – Apply appropriate cleaning procedures.
5. Data Transformation – Standardize formats and restructure data where necessary.
6. Data Validation – Verify cleaned data for accuracy and consistency.
7. Processed Data Storage – Save validated datasets in the appropriate directories.
8. Analytical Usage – Use processed datasets for analysis and dashboard development.

5. Data Quality Standards

The following checks should be completed before datasets are considered analysis-ready:

Quality Dimension| Validation
Completeness| Assess missing values
Accuracy| Check valid values and geographic coordinates
Consistency| Verify column formats and categorical values
Uniqueness| Inspect duplicate records
Validity| Check data types and permitted value ranges
Integrity| Verify relationships between geographic fields
Timeliness| Document dataset collection and observation periods

All cleaning decisions should be documented, including records removed, values corrected and missing-value treatment.

6. Data Storage Guidelines

1. Never overwrite original datasets in "raw/".
2. Store only cleaned and validated outputs in this directory.
3. Use descriptive and consistent filenames.
4. Maintain the original dataset source information.
5. Document important transformations.
6. Preserve appropriate data types and column definitions.
7. Avoid storing temporary analysis files here.
8. Do not publish confidential or restricted datasets.

7. Data Integration Considerations

The processed business, mobility and pedestrian datasets may support combined geographic analysis.

Before integration:

- Verify geographic compatibility.
- Identify common geographic identifiers.
- Check coordinate reference systems where spatial matching is used.
- Document spatial matching methods and tolerances.
- Examine differences in observation periods.
- Avoid unsupported joins based on row numbers or approximate location similarities.

Datasets should remain separate when a reliable integration key is unavailable.

8. Usage in Analytical Tools

The processed datasets are intended for use in:

Python

- Data manipulation.
- Exploratory data analysis.
- Statistical analysis.
- Geographic analysis.

SQL

- Data querying.
- Aggregations.
- Geographic comparisons where supported by the schema.

Power BI

- Business distribution dashboards.
- Smart mobility dashboards.
- Pedestrian activity dashboards.
- Retail opportunity assessment.

9. Dataset Limitations

- Cleaning does not guarantee that every source record is accurate.
- Missing values may remain when reliable replacement is not possible.
- Geographic coverage may differ between datasets.
- Mobility observations represent the available recorded period.
- Pedestrian counts represent surveyed locations and historical periods.
- Business records should not automatically be interpreted as currently operating establishments.
- Combined analysis requires compatible geographic and temporal coverage.

10. Expected Outputs

The "processed/" directory is expected to contain:

- Cleaned business dataset.
- Cleaned smart mobility dataset.
- Structured pedestrian counts dataset.
- Standardized analytical columns.
- Validated geographic information.
- Documentation of preprocessing decisions.

11. Conclusion

The "processed/" directory provides standardized and validated datasets for the analytical stages of GeoPulse.

Maintaining cleaned datasets separately from original data improves reproducibility, supports reliable analysis and provides a consistent foundation for developing interactive dashboards.

---

Project: GeoPulse – Hyper-Local Retail Mobility Analytics

Organization: Infotact Solutions

Domain: Data Analytics

Documentation: Processed Dataset Management

Tagline: GeoPulse – Turning Location Data into Business Intelligence.

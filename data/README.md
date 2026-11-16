GeoPulse – Data Documentation

1. Overview

The "data/" directory contains all datasets used throughout the GeoPulse – Hyper-Local Retail Mobility Analytics project.

This directory maintains a structured approach to storing, organizing, documenting and managing datasets used for business geographic analysis, smart mobility analysis and pedestrian activity analysis.

The data pipeline separates original datasets from intermediate files and cleaned datasets to maintain data traceability, consistency and reproducibility.

2. Project Datasets

GeoPulse uses three primary datasets.

2.1 Business Dataset

Purpose: To analyze the geographic distribution and concentration of businesses across different locations.

Important attributes:

Column| Description
Business Name| Name of the recorded business
City| City associated with the business
ZIP Code| Postal area identifier
Borough| Administrative geographic area
Community Board| Community board identifier
Council District| Council district identifier
Census Tract| Census geographic identifier
Latitude| Geographic latitude
Longitude| Geographic longitude

Planned analysis:

- Business distribution by borough.
- Business concentration by ZIP code.
- Geographic visualization of business locations.
- Comparison of business distribution across administrative areas.

2.2 Smart Mobility Dataset

Purpose: To examine traffic conditions, vehicle activity and mobility-related observations.

Important attributes:

Column| Description
Timestamp| Date and time of observation
Latitude| Observation latitude
Longitude| Observation longitude
Vehicle_Count| Recorded vehicle count
Traffic_Speed_kmh| Recorded traffic speed
Road_Occupancy_%| Recorded road occupancy percentage
Traffic_Light_State| Traffic signal state
Weather_Condition| Weather condition
Accident_Report| Accident-report field
Ride_Sharing_Demand| Ride-sharing demand
Parking_Availability| Parking availability
Emission_Levels_g_km| Recorded emission level
Traffic_Condition| Traffic condition category

Planned analysis:

- Vehicle count analysis.
- Average traffic speed analysis.
- Road occupancy analysis.
- Traffic condition distribution.
- Weather and traffic pattern comparison.
- Parking and mobility analysis.

2.3 Pedestrian Counts Dataset

Purpose: To understand historical pedestrian activity across surveyed streets and locations.

Important attributes:

Column| Description
Borough| Administrative geographic area
Street_Name| Name of the surveyed street
From_Street| Starting street reference
To_Street| Ending street reference
Historical AM columns| Morning pedestrian counts
Historical MD columns| Midday pedestrian counts
Historical PM columns| Evening pedestrian counts

Planned analysis:

- Morning, midday and evening pedestrian comparisons.
- Pedestrian activity by borough.
- Identification of streets with higher recorded pedestrian counts.
- Historical pedestrian activity analysis.

Historical count columns will be transformed into a structured format during preprocessing where appropriate.

3. Directory Structure

3.1 raw/

Contains original datasets collected or downloaded from their respective sources.

Purpose:

- Preserve original data.
- Maintain data source traceability.
- Support reproducible preprocessing.
- Prevent accidental modification of source files.

Original datasets should remain unchanged.

3.2 interim/

Contains temporary or intermediate datasets generated during preprocessing and transformation.

Purpose:

- Store partially cleaned datasets.
- Maintain intermediate transformation outputs.
- Support validation and quality checks.
- Separate temporary outputs from final analytical datasets.

3.3 processed/

Contains cleaned, validated and analysis-ready datasets.

Purpose:

- Store datasets after preprocessing.
- Maintain consistent data formats.
- Support exploratory data analysis.
- Provide suitable inputs for Power BI dashboards and analytical reports.

3.4 external/

Contains supplementary datasets obtained from external sources that may support additional analysis.

Purpose:

- Store supporting geographic or reference data.
- Maintain external data source documentation.
- Support additional analytical requirements.

4. Data Processing Workflow

The GeoPulse data management workflow follows these stages:

1. Data Collection – Obtain the required datasets.
2. Raw Data Storage – Preserve original datasets in "raw/".
3. Data Inspection – Examine structure, columns, formats and data types.
4. Data Quality Assessment – Identify missing values, duplicates, invalid values and inconsistencies.
5. Data Cleaning – Apply appropriate cleaning and transformation techniques.
6. Intermediate Storage – Save relevant intermediate outputs in "interim/".
7. Data Validation – Verify the quality and consistency of transformed datasets.
8. Processed Data Storage – Store validated datasets in "processed/".
9. Data Analysis – Use processed datasets for Python analysis, SQL queries and Power BI dashboards.

5. Data Quality Standards

The following quality checks should be considered during preprocessing:

- Missing value identification and handling.
- Duplicate record detection.
- Data type validation.
- Geographic coordinate validation.
- Invalid and inconsistent value detection.
- Date and timestamp standardization.
- Numeric range validation.
- Verification of measurement units.
- Dataset completeness assessment.

Cleaning decisions must be documented. Records should not be removed automatically without considering their analytical importance.

6. Data Integration Strategy

The three primary datasets represent different aspects of the retail and mobility environment.

Potential integration dimensions include:

- Geographic location.
- Borough.
- ZIP code.
- Other validated geographic identifiers.

Datasets should only be joined when their geographic identifiers are compatible and the relationship is clearly documented.

Latitude and longitude matching should use a defined spatial matching method and an appropriate tolerance.

Row numbers or approximate geographic similarities must not be treated as reliable join keys.

7. Data Management Guidelines

1. Never overwrite original raw datasets.
2. Maintain separate raw, interim and processed directories.
3. Use descriptive and consistent filenames.
4. Document dataset sources and collection dates.
5. Record important cleaning and transformation decisions.
6. Validate datasets before using them in dashboards.
7. Avoid uploading confidential or restricted datasets to public repositories.
8. Keep large files outside GitHub when repository size or licensing restrictions require it.

8. Dataset Limitations

- Business records do not automatically represent currently operating businesses.
- Mobility observations represent the available recorded period.
- Pedestrian counts represent surveyed streets and historical survey periods.
- Missing geographic information may limit spatial analysis.
- Different datasets may have different collection periods and geographic coverage.
- Correlation between business concentration and pedestrian activity does not establish causation.

9. Expected Outputs

The data directory supports the creation of:

- Cleaned business datasets.
- Processed smart mobility datasets.
- Structured pedestrian count datasets.
- Data quality assessment reports.
- Exploratory data analysis outputs.
- Geographic analysis results.
- Power BI dashboard datasets.

10. Conclusion

The "data/" directory provides a structured foundation for managing the datasets used in GeoPulse.

By maintaining clear separation between original, intermediate and processed data, the project improves data traceability, analytical reliability and reproducibility.

GeoPulse – Turning Location Data into Business Intelligence.

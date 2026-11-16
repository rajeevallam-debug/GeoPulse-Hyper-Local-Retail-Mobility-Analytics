Raw Data – GeoPulse

1. Overview

The "raw/" directory contains the original datasets collected and used for the GeoPulse – Hyper-Local Retail Mobility Analytics project.

These datasets serve as the primary data sources for business geographic analysis, smart mobility analysis and pedestrian activity analysis.

The raw data directory maintains the original structure and content of collected datasets before any cleaning, transformation or preprocessing activities.

2. Purpose

The purpose of this directory is to:

- Preserve original datasets without modification.
- Maintain data source traceability.
- Provide a reference for data quality assessment.
- Support reproducible data preprocessing.
- Maintain consistency between original and processed datasets.
- Enable verification of analytical results.

3. Dataset Organization

The raw datasets are organized into three categories.

3.1 Business Dataset

Directory: "businesses/"

Purpose: Contains business-related geographic information used to examine retail distribution and business concentration across different locations.

Important attributes:

Attribute| Description
Business Name| Recorded business name
City| City associated with the business
ZIP Code| Postal area identifier
Borough| Administrative geographic area
Community Board| Community board identifier
Council District| Council district identifier
Census Tract| Census geographic identifier
Latitude| Geographic latitude
Longitude| Geographic longitude

Analytical applications:

- Business distribution analysis.
- Borough-wise business comparison.
- ZIP-code-level business concentration.
- Geographic business mapping.

3.2 Smart Mobility Dataset

Directory: "mobility/"

Purpose: Contains traffic and mobility observations used to understand vehicle activity and road conditions.

Important attributes:

Attribute| Description
Timestamp| Observation date and time
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
- Traffic condition analysis.
- Weather and mobility comparison.
- Parking and mobility analysis.

3.3 Pedestrian Counts Dataset

Directory: "pedestrian_counts/"

Purpose: Contains historical pedestrian count observations across surveyed streets and locations.

Important attributes:

Attribute| Description
Borough| Administrative geographic area
Street_Name| Surveyed street name
From_Street| Starting street reference
To_Street| Ending street reference
AM columns| Morning pedestrian counts
MD columns| Midday pedestrian counts
PM columns| Evening pedestrian counts

Analytical applications:

- Pedestrian activity analysis.
- Morning, midday and evening comparisons.
- Street-level pedestrian analysis.
- Borough-wise pedestrian comparison.
- Historical footfall analysis.

4. Data Source Management

Each original dataset should have its source information documented.

Recommended metadata:

Metadata| Description
Dataset Name| Original dataset name
Source| Website, organization or provider
Download Date| Date of dataset collection
File Format| CSV, XLSX or other format
Original Filename| Name of the downloaded file
Record Count| Number of records
Description| Brief dataset explanation
License| Applicable usage or distribution terms

Where source information is unavailable, record it as unknown rather than assuming a source.

5. Raw Data Handling Guidelines

The following rules must be followed:

1. Original datasets must never be directly modified.
2. Data cleaning must be performed on separate working copies.
3. Original column names should be preserved in raw files.
4. Original file formats should be maintained whenever possible.
5. Dataset sources and collection dates should be documented.
6. Raw datasets should not contain manually modified analytical results.
7. Confidential or restricted datasets must not be uploaded to public repositories.
8. Large datasets should be managed according to GitHub storage limitations.

6. Data Quality Assessment

Before preprocessing, the following checks should be performed:

- Dataset structure inspection.
- Column name verification.
- Missing value identification.
- Duplicate record detection.
- Data type inspection.
- Invalid geographic coordinate identification.
- Numeric range validation.
- Date and timestamp format verification.
- Measurement unit verification.

These checks help identify potential data quality issues before analytical processing.

7. Relationship with Other Data Directories

Directory| Responsibility
"raw/"| Stores original datasets
"interim/"| Stores intermediate datasets
"processed/"| Stores cleaned and validated datasets
"external/"| Stores supplementary external datasets

The processing workflow follows:

Raw Data → Data Inspection → Data Cleaning → Data Validation → Processed Data → Analysis

8. Important Considerations

- Raw data should remain unchanged throughout the project.
- Missing values should be evaluated before deciding how to handle them.
- Duplicate records should be investigated before removal.
- Geographic coordinates should be validated before mapping.
- Different datasets may have different geographical coverage and observation periods.
- Business records should not automatically be interpreted as currently operating businesses.
- Data integration should only be performed using compatible geographic identifiers or documented spatial matching methods.

9. Expected Outcome

The "raw/" directory provides a reliable reference for all original datasets used in GeoPulse.

Maintaining original datasets separately improves traceability, supports reproducible preprocessing and helps ensure that analytical results can be verified against their source data.

---

Project: GeoPulse – Hyper-Local Retail Mobility Analytics

Organization: Infotact Solutions

Domain: Data Analytics

Documentation: Raw Dataset Management

Tagline: GeoPulse – Turning Location Data into Business Intelligence.

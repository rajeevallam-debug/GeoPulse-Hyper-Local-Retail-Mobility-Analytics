GeoPulse – Source Code (src/)
Purpose
The src/ folder contains the reusable Python modules for preparing, validating, analysing, and supporting visualisation of the GeoPulse datasets.
The current workbook, GeoPulse_Cleaned_Data_Quality_FIXED.xlsx, contains these data sheets:
Businesses_dataset_20261111 – business locations and administrative/geographic attributes, including latitude and longitude.
smart_mobility_dataset – timestamped mobility observations such as vehicle count, traffic speed, road occupancy, traffic-light state, weather, accidents, parking availability, emissions, energy consumption, and traffic condition.
Bi-Annual_Pedestrian_Counts_202 – pedestrian counts by location, street, survey period, and time of day.
DQ_Summary, Field_Quality, and DQ_Findings – data-quality summaries, field-level quality information, and documented findings/recommendations.
Recommended structure
src/
├── README.md
├── config.py
├── data_loader.py
├── data_cleaning.py
├── data_validation.py
├── geospatial_analysis.py
├── mobility_analysis.py
├── pedestrian_analysis.py
└── utils.py
Module responsibilities
Module	Responsibility
config.py	"Store project paths, input workbook name, and shared configuration."
data_loader.py	Load the required Excel sheets into pandas DataFrames.
data_cleaning.py	Apply documented cleaning steps while preserving source data and recording changes.
data_validation.py	"Check missing values, duplicate records, data types, ranges, and required columns."
geospatial_analysis.py	"Support location-based analysis using latitude, longitude, borough, and street fields."
mobility_analysis.py	"Analyse traffic volume, speed, occupancy, traffic conditions, emissions, and energy consumption."
pedestrian_analysis.py	"Analyse pedestrian counts across locations, survey periods, and time-of-day columns."
utils.py	Provide shared helper functions used by other modules.


Expected workflow
Load the workbook from the project's data/ directory.
Select the required dataset sheet.
Validate column names, data types, missing values, duplicates, and plausible value ranges.
Apply only justified cleaning operations; do not automatically replace all missing values.
Generate analysis-ready outputs for notebooks or the dashboard.
Record important processing decisions and validation results.
Example data-loading approach
import pandas as pd
from pathlib import Path

DATA_FILE = Path("data/GeoPulse_Cleaned_Data_Quality_FIXED.xlsx")

businesses = pd.read_excel(
    DATA_FILE,
    sheet_name="Businesses_dataset_20261111"
)

mobility = pd.read_excel(
    DATA_FILE,
    sheet_name="smart_mobility_dataset"
)

pedestrian = pd.read_excel(
    DATA_FILE,
    sheet_name="Bi-Annual_Pedestrian_Counts_202"
)
Run this example from the project root, or update DATA_FILE to match the actual workbook location.
Development guidelines
Keep raw input data unchanged.
Keep data loading, cleaning, validation, and analysis in separate modules.
Use clear function names and document function inputs and outputs.
Avoid hard-coded machine-specific file paths.
Handle missing values according to the analysis requirement and document the decision.
Validate geographic coordinates before mapping: latitude should be between -90 and 90, and longitude between -180 and 180.
Do not treat correlation or observed patterns as proof of causation.
Add tests for reusable functions and update this README when the source structure changes.
Dependencies
The modules are expected to use:
pandas
numpy
openpyxl
Install project dependencies from the repository root using:
pip install -r requirements.txt
Current implementation status
This README defines the recommended source-code structure and responsibilities. The module files listed above are planned components; create and test each module as its implementation is added to the project.

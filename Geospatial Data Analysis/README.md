# 📊 Geospatial Data Analysis — Regional Market Expansion in India

## 📌 Project Overview

This project analyzes synthetic regional market data to identify potential business expansion opportunities across Indian cities and states. It uses geographic coordinates and market indicators to visualize regional patterns, compare demand and competition, and shortlist high-potential underserved market candidates.

The project was completed as part of the **Workora Virtual Internship**.

## 🎯 Objectives

- Clean and validate regional market data.
- Analyze monthly search demand and existing competition by geographic region.
- Compare regional conversion rates, income levels, and estimated customer acquisition costs.
- Create an interactive geographic map of market locations using Folium.
- Identify the top three potential expansion regions using a transparent opportunity scoring method.
- Generate a spatial analysis report for business decision-making.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Pandas** — Data cleaning and regional aggregation
- **NumPy** — Numerical operations
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical visualization
- **Folium** — Interactive geographic mapping
- **Branca** — Map color scales
- **Jupyter Notebook** — Analysis environment
- **ReportLab** — PDF report generation

## 📂 Project Structure

```text
Geospatial Data Analysis/
│
├── data/
│   └── india_regional_market_v2.csv
│
├── notebooks/
│   └── Analysis.ipynb
│   └── output/
│      ├── regional_market_map.html
│      ├── Geospatial_Analysis_Report.pdf
│      ├── cleaned_regional_market_data.csv
│      ├── state_market_summary.csv
│      └── top_3_expansion_regions.csv
│
├── .gitignore
├── README.md
└── requirements.txt
```

## 📊 Dataset Description

**Dataset:** `india_regional_market_v2.csv`

The original dataset contains 400 regional records and 11 columns.

| Column | Description |
|---|---|
| `RegionID` | Unique regional record identifier |
| `City` | City associated with the record |
| `State` | Indian state associated with the record |
| `Latitude` | Latitude coordinate |
| `Longitude` | Longitude coordinate |
| `PopulationSegment` | Population or customer segment |
| `MonthlySearchDemand` | Estimated monthly search demand |
| `ExistingCompetitors` | Number of existing competitors |
| `MedianAnnualIncomeINR` | Median annual income estimate in INR |
| `LeadConversionRate` | Estimated lead conversion rate |
| `EstimatedAcquisitionCostINR` | Estimated customer acquisition cost in INR |

**Data quality:** Initial inspection found no missing values or duplicate rows in the supplied dataset.

**Important:** The dataset is synthetic and intended for learning and analytical practice. Its figures should not be interpreted as verified real-world market measurements.

## 🔍 Project Workflow

### 1. Data Cleaning and Validation

- Inspected dataset dimensions, columns, and data types.
- Checked for missing values and duplicate records.
- Standardized whitespace in text columns.
- Checked unique region identifiers.
- Validated latitude and longitude against broad geographic bounds for India.
- Checked market indicators for invalid values.

### 2. Regional Market Analysis

Aggregated regional indicators by state to compare:

- Total monthly search demand
- Average monthly search demand
- Number of regions and cities represented
- Average number of competitors
- Average lead conversion rate
- Average annual income
- Average acquisition cost
- Average market opportunity score

### 3. Opportunity Scoring

A relative market opportunity score was calculated using normalized indicators:

- **50% — Monthly search demand**
- **30% — Low competition**
- **20% — Lead conversion rate**

The score is calculated as:

`Opportunity Score = (0.50 × Demand Score) + (0.30 × Low Competition Score) + (0.20 × Conversion Score)`

The indicators are normalized to a scale from 0 to 1. The low-competition score reverses the normalized competitor count so that fewer competitors produce a higher score.

Acquisition cost is assessed separately when comparing shortlisted regions.

This is a screening metric, not a validated prediction of revenue, profitability, or expansion success.

### 4. Geographic Visualization

An interactive map was created using Folium.

The map includes:

- Geographic markers based on supplied latitude and longitude.
- Marker clustering for easier navigation.
- Color-coded opportunity scores.
- Pop-ups containing regional demand, competition, conversion rate, income, and acquisition cost.
- A color scale to compare relative opportunity scores.

### 5. Expansion Opportunity Identification

Regions were shortlisted using the following initial criteria:

- Monthly search demand at or above the 75th percentile.
- Existing competitor count at or below the median.

Eligible candidates were then ranked by opportunity score. Conversion rate and estimated acquisition cost provide additional context for reviewing the final recommendations.

The resulting top three are **potential expansion candidates**, not confirmed underserved markets.

## 📈 Key Deliverables

| Deliverable | Description |
|---|---|
| `analysis.ipynb` | Complete data cleaning, analysis, visualization, and scoring workflow |
| `regional_market_map.html` | Interactive geographic market map |
| `Geospatial_Analysis_Report.pdf` | Spatial analysis report and regional recommendations |
| `cleaned_regional_market_data.csv` | Cleaned regional dataset with calculated scores |
| `state_market_summary.csv` | Aggregated state-level indicators |
| `top_3_expansion_regions.csv` | Shortlist of the highest-ranked eligible candidates |

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or later
- Jupyter Notebook or Visual Studio Code
- The supplied regional CSV dataset

### Step 1: Clone the repository

```bash
git clone https://github.com/Apxsingh/Workora-Internship-tasks-Arpitsinghtomar/tree/main/Geospatial%20Data%20Analysis

cd "Geospatial Data Analysis"
```


### Step 2: Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv geo_env
.\geo_env\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
python3 -m venv geo_env
source geo_env/bin/activate
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Launch Jupyter Notebook

```bash
jupyter notebook
```

Open `analysis.ipynb` and run the cells sequentially.

Ensure the original dataset is available at:

```text
data/india_regional_market_v2.csv
```

## 🗺️ Viewing the Interactive Map

After running the notebook, open:

```text
output/regional_market_map.html
```

Open the file in a modern web browser and explore the regional markers, market indicators, and opportunity scores.

The map uses supplied coordinates and an online basemap tile service, so an internet connection may be needed for the background map.

## 📑 Viewing the Report

Open:

```text
output/Geospatial_Analysis_Report.pdf
```

The report summarizes the methodology, state-level comparisons, shortlisted expansion candidates, and key limitations.

## ⚠️ Limitations

- The dataset is synthetic and does not represent verified real-world market conditions.
- Direct sales and revenue data are not available; search demand is used as a demand proxy.
- Competitor counts do not directly measure market saturation or actual unmet demand.
- Geographic checks use broad bounds and do not independently verify city boundaries.
- Opportunity scores depend on the selected weights and normalization method.
- The analysis does not establish causal relationships or guarantee commercial success.

## 🚀 Future Improvements

- Integrate verified geographic boundary data for state-level choropleth maps.
- Incorporate actual sales, customer density, and market penetration data.
- Use spatial clustering techniques such as DBSCAN to detect geographic demand clusters.
- Test alternative scoring weights and conduct sensitivity analysis.
- Develop a dashboard using Streamlit, Tableau, or Power BI.
- Validate shortlisted locations with real-world market research.

## 👨‍💻 Author

**Arpit Singh Tomar**

B.Tech Computer Science and Engineering

GitHub: [@Apxsingh](https://github.com/Apxsingh)

## 📄 License and Data Usage

This project was developed for educational and internship purposes. Refer to the dataset provider's terms before redistributing the original dataset or using it for commercial purposes.

---

**Project Status:** Completed — Geospatial Data Analysis and Regional Market Opportunity Screening.
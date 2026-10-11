# Workora Internship Tasks — Data Analytics & Machine Learning

A collection of data analytics, statistical testing, business intelligence, and machine learning projects completed as part of the Workora internship.

This repository demonstrates practical skills in Python programming, data cleaning, exploratory data analysis, statistical hypothesis testing, data visualization, geographic analysis, dashboard development, and predictive modeling.

**Author:** Arpit Singh Tomar  
**Education:** B.Tech Computer Science and Engineering  
**GitHub:** [@Apxsingh](https://github.com/Apxsingh)  
**Focus Areas:** Data Analytics · Machine Learning · Artificial Intelligence · Software Development

---

## Table of Contents

- [About the Repository](#about-the-repository)
- [Project Portfolio](#project-portfolio)
- [Technology Stack](#technology-stack)
- [Skills Demonstrated](#skills-demonstrated)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Data and Results Disclaimer](#data-and-results-disclaimer)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## About the Repository

This repository brings together seven independent projects covering different stages of the data analytics and machine learning lifecycle.

The projects range from foundational data quality validation and statistical analysis to interactive dashboards and predictive customer churn modeling.

Each project has its own dataset, analysis workflow, dependencies, and deliverables. Depending on the project, the outputs include Jupyter Notebooks, visualizations, CSV reports, PDF reports, trained machine learning models, and an interactive dashboard.

## Project Portfolio

### 1. A/B Testing & Hypothesis Testing

**Category:** Statistical Analysis · Experimentation

[Open Project Folder](./AB%20Testing%20%26%20Hypothesis%20Testing/)

Analyzes a website checkout experiment to compare Variant A and Variant B and determine whether their observed conversion rates differ statistically.

**Key work:**
- Data cleaning and validation of 1,200 visitor records.
- Conversion-rate calculation and absolute and relative conversion lift.
- Two-proportion z-test and chi-square test of independence.
- Confidence intervals and Cohen's h effect size.
- Device and traffic-source segmentation.
- Revenue analysis, visualizations, and PDF reporting.

**Tools:** Python, Pandas, NumPy, SciPy, Statsmodels, Matplotlib, Seaborn.

**Deliverables:** Jupyter Notebook, conversion charts, statistical analysis, and PDF report.

**Objective:** Support evidence-based decisions about checkout optimization while distinguishing statistical significance from practical business impact.

---

### 2. Customer Churn Analysis

**Category:** Data Analytics · Customer Retention

[Open Project Folder](./Customer%20Churn%20Analysis/)

Analyzes customer subscription data to identify churn patterns and evaluate retention-related metrics.

**Key work:**
- Data inspection, cleaning, and churn-flag encoding.
- Churn rate, Monthly Recurring Revenue (MRR) loss, and estimated Customer Lifetime Value (CLV).
- Churn segmentation by contract type, tenure, payment method, subscription type, and support tickets.
- Correlation analysis and comparisons between churned and retained customers.
- Visualizations and a business-oriented analytics report.

**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook.

**Reported dataset:** 15 customer records.

**Reported results from the supplied sample:**

| Metric | Result |
|---|---:|
| Customers | 15 |
| Churned customers | 7 |
| Churn rate | 46.67% |
| Total MRR | ₹1,269.85 |
| MRR lost | ₹409.93 |
| Estimated CLV | ₹1,591.55 |

**Deliverables:** Analysis notebook, charts, and customer churn analysis PDF report.

**Important:** These results come from a very small sample and should be treated as illustrative rather than representative of a larger customer population.

---

### 3. Data Cleaning & Structural Validation

**Category:** Data Quality · Data Preparation

[Open Project Folder](./Data%20Cleaning%20%26%20Structural%20Validation/)

Demonstrates a structured data-quality workflow to validate customer data before further analysis.

**Key work:**
- Dataset inspection using shape, column names, data types, and descriptive statistics.
- Missing-value and duplicate-record checks.
- Numerical validation for age, tenure, charges, and support tickets.
- Categorical-value consistency checks.
- Customer ID uniqueness validation.
- Charge consistency checks.
- Column-name standardization and whitespace removal.
- Export of the cleaned dataset and a cleaning summary.

**Tools:** Python, Pandas, Jupyter Notebook.

**Reported results:**

- Initial dataset: 15 rows and 11 columns.
- Missing values detected: 0.
- Duplicate rows detected: 0.
- Duplicate customer IDs detected: 0.
- Final dataset: 15 rows and 11 columns.

**Deliverables:** Data-cleaning notebook and `cleaned_customer_data.csv`.

**Objective:** Establish a reliable and reproducible foundation for downstream analytics.

---

### 4. Geospatial Data Analysis — Regional Market Expansion in India

**Category:** Geospatial Analytics · Market Research

[Open Project Folder](./Geospatial%20Data%20Analysis/)

Uses geographic coordinates and regional market indicators to shortlist potential expansion opportunities across Indian cities and states.

**Key work:**
- Cleaning and validation of 400 regional records.
- Geographic coordinate validation.
- State-level aggregation of market indicators.
- Comparison of search demand, competition, conversion rates, income, and acquisition costs.
- Relative market opportunity scoring.
- Interactive geographic visualization using Folium.
- Shortlisting of three potential expansion candidates.

**Opportunity scoring approach:**

- 50% — Normalized monthly search demand.
- 30% — Normalized low-competition score.
- 20% — Normalized lead conversion rate.

Acquisition cost is considered separately when reviewing shortlisted regions.

**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, Folium, Branca, ReportLab.

**Deliverables:**
- Interactive regional market map.
- Cleaned regional market dataset.
- State-level summary CSV.
- Top-three expansion candidate CSV.
- Geospatial analysis PDF report.

**Objective:** Demonstrate how geographic and market indicators can support preliminary business expansion decisions.

**Disclaimer:** The dataset is synthetic, and the opportunity score is a screening metric rather than a validated measure of commercial success.

---

### 5. Interactive Business Intelligence Dashboard

**Category:** Business Intelligence · Interactive Visualization

[Open Project Folder](./Interactive%20Dashboard%20Development/)

Develops an interactive Streamlit dashboard that brings together four independent analytical datasets.

**Dashboard sections:**

- **Executive Overview:** Summary KPIs and key indicators.
- **Web Traffic & Acquisition:** Traffic sources, engagement, bounce rate, and conversion behavior.
- **Customer Churn:** Retention metrics and churn segmentation.
- **Checkout A/B Testing:** Conversion performance and revenue comparisons.
- **Regional Market Analysis:** Geographic market indicators and an interactive map.
- **Data Quality & Assumptions:** Data cleaning information, limitations, and dataset previews.

**Key features:**
- Interactive filters.
- KPI summary cards.
- Plotly visualizations.
- Geographic mapping.
- Filtered CSV exports.
- Data-quality documentation.

**Tools:** Python, Streamlit, Pandas, Plotly Express, Git, GitHub, Streamlit Community Cloud.

**Datasets:** Web traffic, customer churn, checkout A/B testing, and regional market data.

**Deliverables:** Streamlit application, requirements file, screenshots, and deployment link or demonstration video.

**Deployment status:** Add the verified public dashboard URL after successful deployment.

**Objective:** Demonstrate how separate analytical workflows can be presented through one interactive business intelligence interface without making unsupported joins between unrelated datasets.

---

### 6. Predictive Churn Analysis

**Category:** Machine Learning · Classification

[Open Project Folder](./Predictive%20Churn%20Analysis/)

Builds a classification pipeline to predict customer churn using demographic, subscription, billing, and customer-support features.

**Dataset:** `customer_churn_model_v2.csv`

The dataset contains 800 records and 13 original columns.

**Key work:**
- Data inspection and validation.
- Target encoding: `No = 0`, `Yes = 1`.
- Numerical preprocessing using median imputation and MinMax scaling.
- Categorical preprocessing using most-frequent imputation and One-Hot Encoding.
- Stratified 80/20 train-test split.
- Training and comparison of Logistic Regression and Random Forest.
- Confusion matrices, classification reports, and ROC curves.
- Customer churn probability estimates and risk categorization.
- Export of evaluation results and the trained model.

**Tools:** Python, Pandas, NumPy, Scikit-learn, Matplotlib, Joblib, Jupyter Notebook.

**Initial test-set results:**

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 66.9% | 63.7% |
| Precision | 58.3% | 55.7% |
| Recall | 73.1% | 65.7% |
| F1 Score | 0.649 | 0.603 |
| ROC-AUC | 0.681 | 0.658 |

**Current best model:** Logistic Regression, based on the highest ROC-AUC among the two evaluated models.

**Deliverables:**
- Executed Jupyter Notebook.
- Customer churn-risk predictions CSV.
- Model evaluation metrics CSV and JSON.
- Trained model pipeline.
- Project summary and evaluation visualizations.

**Objective:** Demonstrate an end-to-end machine learning pipeline that converts customer data into interpretable churn-risk predictions.

**Limitations:** Results are based on a single held-out test set of 160 records. Additional validation, cross-validation, threshold tuning, and probability calibration are recommended before practical deployment.

---

### 7. Web Traffic Analytics

**Category:** Web Analytics · Performance Measurement

[Open Project Folder](./Web%20Traffic%20Analytics/)

Analyzes session-level website traffic to understand engagement, acquisition channels, page performance, and conversion behavior.

**Key work:**
- Data inspection and structural validation.
- Session and conversion data cleaning.
- Bounce-rate calculation.
- Average session duration.
- Average pageviews per session.
- Conversion-rate comparisons by traffic channel.
- Page-level session and conversion analysis.
- Chart generation and PDF dashboard reporting.

**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook.

**Key metrics:**

| Metric | Purpose |
|---|---|
| Bounce Rate | Measures the proportion of sessions classified as bounced |
| Average Session Duration | Measures session engagement time |
| Conversion Rate | Measures the proportion of sessions that convert |
| Pageviews per Session | Measures browsing activity per session |
| Sessions by Channel | Compares traffic acquisition volume |
| Page-Level Performance | Identifies pages requiring further investigation |

**Deliverables:** Jupyter Notebook, traffic-channel summary, page-performance summary, charts, and PDF dashboard.

**Objective:** Demonstrate how web analytics metrics can support data-informed improvements to website engagement and conversion.

**Limitation:** The supplied sample contains only 10 sessions. Results are illustrative, and the available data does not support reliable sequential page-to-page funnel analysis.

---

## Technology Stack

| Area | Technologies |
|---|---|
| Programming | Python |
| Data manipulation | Pandas, NumPy |
| Statistical testing | SciPy, Statsmodels |
| Machine learning | Scikit-learn |
| Data visualization | Matplotlib, Seaborn, Plotly Express |
| Geospatial analysis | Folium, Branca |
| Interactive dashboards | Streamlit |
| Notebooks | Jupyter Notebook, VS Code |
| Reporting | ReportLab, PDF and CSV exports |
| Model persistence | Joblib |
| Version control | Git, GitHub |
| Deployment | Streamlit Community Cloud |

---

## Skills Demonstrated

### Data Analytics
- Data cleaning and validation.
- Exploratory data analysis.
- Aggregation and segmentation.
- KPI calculation and interpretation.
- Business-oriented reporting.

### Statistics and Experimentation
- Hypothesis formulation.
- Statistical significance testing.
- Confidence intervals and effect sizes.
- Conversion lift analysis.
- Interpretation of experimental results.

### Machine Learning
- Feature preprocessing.
- One-Hot Encoding and numerical scaling.
- Classification model training.
- Model evaluation and comparison.
- Churn-risk prediction.
- Model serialization and export.

### Visualization and Applications
- Static and interactive charts.
- Geographic data visualization.
- Interactive dashboard development.
- PDF and CSV report generation.
- Reproducible notebook-based workflows.

---

## Repository Structure

```text
Workora-Internship-tasks-Arpitsinghtomar/
│
├── AB Testing & Hypothesis Testing/
│   ├── data/
│   ├── notebook/
│   ├── README.md
│   ├── .gitignore
│   └── requirements.txt
│
├── Customer Churn Analysis/
│   ├── data/
│   ├── images/
│   ├── notebook/
│   ├── report/
│   ├── README.md
│   └── requirements.txt
│
├── Data Cleaning & Structural Validation/
│   ├── data/
│   ├── notebook/
│   ├── README.md
│   └── requirements.txt
│
├── Geospatial Data Analysis/
│   ├── data/
│   ├── notebooks/
│   ├── README.md
│   └── requirements.txt
│
├── Interactive Dashboard Development/
│   ├── data/
│   ├── screenshots/
│   ├── app.py
│   ├── README.md
│   └── requirements.txt
│
├── Predictive Churn Analysis/
│   ├── data/
│   ├── notebook/
│   ├── README.md
│   └── requirements.txt
│
├── Web Traffic Analytics/
│   ├── data/
│   ├── outputs/
│   ├── web_traffic_analysis.ipynb
│   ├── README.md
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

*Note: This is a representative structure. Actual notebook names, generated artifacts, and additional files may differ between project folders.*

---

## Getting Started

Each project is designed to run independently and may have its own dependencies.

### Prerequisites

- Python 3.10 or a compatible version required by the selected project.
- pip.
- Git.
- Visual Studio Code with the Python and Jupyter extensions, or Jupyter Notebook.

### 1. Clone the repository

```bash
git clone https://github.com/Apxsingh/Workora-Internship-tasks-Arpitsinghtomar.git
cd Workora-Internship-tasks-Arpitsinghtomar
```

### 2. Navigate to a project

For example, to explore the predictive churn project:

```powershell
cd "Predictive Churn Analysis"
```

### 3. Create a virtual environment

```powershell
python -m venv PCA_env
.\PCA_env\Scripts\Activate.ps1
```

Use the environment name and activation command documented in the selected project's README when they differ.

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the project

For notebook-based projects, open the notebook in VS Code or Jupyter and execute its cells in order.

For the interactive dashboard:

```bash
python -m streamlit run app.py
```

Follow the individual project's README for dataset paths, additional setup, output locations, and deployment instructions.

---

## Data and Results Disclaimer

- The supplied internship datasets may be synthetic and should not automatically be treated as real-world business data.
- Reported metrics are specific to the dataset and analysis method used in each project.
- Statistical significance does not necessarily imply practical business significance.
- Predictive models are experimental and should not be considered production-ready without additional validation.
- Market opportunity scores are screening tools, not guarantees of commercial success.
- Interactive dashboards and public deployment links should be considered available only after they have been successfully tested and verified.

---

## Future Improvements

- Add automated data validation and testing to each project.
- Improve reproducibility through consistent environment and dependency management.
- Extend model evaluation with cross-validation and hyperparameter tuning.
- Improve dashboard accessibility, deployment reliability, and documentation.
- Add verified screenshots, reports, and public application links.
- Explore additional machine learning and statistical techniques where supported by the data.
- Develop more comprehensive reporting and monitoring workflows.

---

## Author

**Arpit Singh Tomar**

B.Tech Computer Science and Engineering

Interests: Data Analytics, Machine Learning, Artificial Intelligence, and Software Development.

- GitHub: [Apxsingh](https://github.com/Apxsingh)

---

## Acknowledgment

These projects were developed as part of an internship-style learning experience associated with Workora. They demonstrate the practical application of programming, analytics, statistics, visualization, and machine learning concepts.

If you find this repository useful for learning, feel free to explore the individual project folders and review their notebooks and documented methodologies.

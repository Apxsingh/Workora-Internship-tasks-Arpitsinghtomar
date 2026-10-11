# 📊 Interactive Business Intelligence Dashboard

An interactive business intelligence dashboard developed as part of the **Workora Virtual Internship**. The application uses Python, Streamlit, Pandas, and Plotly to analyze synthetic datasets covering web traffic, customer churn, checkout conversion experiments, and regional market opportunities.

> **Disclaimer:** All records in the supplied datasets are synthetic and intended for educational purposes only. The results must not be interpreted as actual Workora business performance.

## 🎯 Project Objective

Build an interactive dashboard featuring KPI summary cards, dynamic filters, responsive charts, geographic visualization, and data quality documentation.

The dashboard brings four related analytical datasets into one application while keeping their metrics separate where no reliable cross-dataset join key exists.

## ✨ Features

- **KPI Summary Cards:** Total Revenue, Active Sessions, Customer Churn Rate, and Average Order Value.
- **Interactive Filters:** Date range, region, acquisition source, landing page, device, subscription category, market state, and population segment, where applicable.
- **Web Traffic & Acquisition:** Session trends, registration rate, bounce rate, session duration, page views, and landing-page performance.
- **Customer Churn Analysis:** Churn rate by contract type, subscription, and payment method; customer tenure and monthly-charge analysis.
- **Checkout A/B Testing:** Conversion rates, checkout-start rates, revenue per visitor, and order-value distributions for experiment variants.
- **Regional Market Analysis:** Interactive geographic map, monthly search demand, competition, lead conversion, and estimated acquisition cost.
- **Data Quality & Assumptions:** Cleaning audit, missing-value information, documented assumptions, and dataset previews.
- **CSV Downloads:** Export filtered data for further analysis.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Interactive dashboard interface |
| Pandas | Data loading, cleaning, transformation, and analysis |
| Plotly Express | Interactive charts and geographic maps |
| Git & GitHub | Version control and project hosting |
| Streamlit Community Cloud | Public dashboard deployment |

## 📁 Project Structure

```text
Interactive Dashboard Development/
│
├── data/
│   ├── web_traffic.csv
│   ├── customer_churn.csv
│   ├── checkout_ab_test.csv
│   └── regional_market.csv
│
├── app.py
├── inspect_data.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

The `data/` directory contains the four synthetic CSV datasets supplied with the internship task. The `screenshots/` directory can contain dashboard screenshots for documentation.

## 📂 Dataset Descriptions

### 1. Web Traffic — `web_traffic.csv`

Contains 900 rows and 12 columns.

Important fields include:

- `SessionID`
- `Date`
- `LandingPage`
- `Source`
- `Campaign`
- `DeviceCategory`
- `Region`
- `SessionDurationSec`
- `PageViews`
- `StartedRegistration`
- `Registered`
- `Bounced`

**Analysis:** Traffic trends, acquisition sources, engagement, landing-page performance, registration rate, and bounce rate.

### 2. Customer Churn — `customer_churn.csv`

Contains 605 rows and 13 columns before cleaning.

Important fields include:

- `CustomerID`
- `Age`
- `Region`
- `TenureMonths`
- `SubscriptionType`
- `MonthlyChargesINR`
- `TotalChargesINR`
- `ContractType`
- `SupportTickets`
- `LatePayments`
- `PaymentMethod`
- `AutoPay`
- `Churn`

**Analysis:** Customer retention, churn rates, subscription performance, payment-method comparisons, tenure, and monthly charges.

The original dataset contains missing region values, duplicate records, and potential numeric outliers.

### 3. Checkout A/B Test — `checkout_ab_test.csv`

Contains 1,200 rows and 8 columns.

Important fields include:

- `VisitorID`
- `Variant`
- `Timestamp`
- `Device`
- `TrafficSource`
- `CheckoutStarted`
- `Converted`
- `OrderValueINR`

**Analysis:** Checkout conversion rates, checkout starts, revenue, revenue per visitor, and comparisons between experiment variants.

### 4. Regional Market — `regional_market.csv`

Contains 400 rows and 11 columns.

Important fields include:

- `RegionID`
- `City`
- `State`
- `Latitude`
- `Longitude`
- `PopulationSegment`
- `MonthlySearchDemand`
- `ExistingCompetitors`
- `MedianAnnualIncomeINR`
- `LeadConversionRate`
- `EstimatedAcquisitionCostINR`

**Analysis:** Geographic market demand, state-level comparisons, competition, lead conversion, and acquisition costs.

## 📈 KPI Definitions

| KPI | Calculation |
|---|---|
| Total Revenue | Sum of `OrderValueINR` for records where `Converted = Yes` |
| Active Sessions | Number of distinct `SessionID` values in the filtered web traffic data |
| Customer Churn Rate | Valid churned customer records divided by valid Yes/No churn records, multiplied by 100 |
| Average Order Value | Average positive `OrderValueINR` among converted records |

**Metric assumptions:**

- Active Sessions is used as a proxy for the requested Active Users KPI because the traffic dataset does not contain a unique user identifier.
- Average Order Value is used as a proxy for Average Ticket Size because transaction values are available in the checkout dataset.
- Revenue and average order value are calculated from converted checkout records, not from a general accounting ledger.
- Churn is calculated independently from the customer dataset.
- Each metric describes the relevant synthetic dataset and should not be interpreted as a unified business-wide measurement.

## 🧹 Data Cleaning and Preprocessing

The dashboard performs the following cleaning operations when loading the datasets:

### Web Traffic
- Parses the `Date` column into datetime values.
- Converts session duration and page-view fields to numeric values.
- Normalizes Yes/No values.
- Fills missing regions with `Unknown`.
- Removes exact duplicate rows and repeated session IDs, retaining the first occurrence.

### Customer Churn
- Removes exact duplicate rows and repeated customer IDs, retaining the first occurrence.
- Converts numeric fields to numeric data types.
- Replaces missing region values with `Unknown`.
- Normalizes churn and auto-pay labels.
- Retains numeric outliers unless a justified cleaning threshold is established.

### Checkout A/B Test
- Parses timestamps into datetime values.
- Converts order values to numeric values.
- Normalizes conversion and checkout-start labels.
- Removes exact duplicate rows and repeated visitor IDs, retaining the first occurrence.

### Regional Market
- Converts geographic and analytical fields to numeric values.
- Removes exact duplicate rows and repeated region IDs, retaining the first occurrence.
- Excludes records with invalid latitude or longitude values.

### Data Quality Considerations

- Invalid numeric values may become missing during conversion and are handled according to the relevant metric or visualization.
- Missing values are not automatically imputed with arbitrary averages.
- Duplicate handling is based on the dataset's documented unique identifiers.
- Cleaning audit information is available on the dashboard's **Data Quality & Assumptions** page.

## 🔗 Dataset Relationships and Limitations

The four datasets represent separate analytical domains.

| Dataset | Identifier | Primary purpose |
|---|---|---|
| Web traffic | `SessionID` | Acquisition and engagement |
| Customer churn | `CustomerID` | Retention and customer behavior |
| Checkout A/B test | `VisitorID` | Checkout conversion |
| Regional market | `RegionID` | Market demand and geographic opportunity |

No shared customer-level or transaction-level key is documented across all four datasets. Therefore, the dashboard does not perform speculative joins between these identifiers.

The region fields in the traffic and churn datasets are used within their respective analyses; they are not assumed to map directly to the geographic records in the regional market dataset.

The dashboard provides descriptive analysis. It does not establish causal relationships or claim statistical significance for the A/B experiment.

## 🚀 Installation and Local Setup

### Prerequisites

- Python 3.11 or another compatible Python version
- pip
- Git (optional for local execution, required for the GitHub workflow)

### Step 1: Clone the repository

After pushing this project to GitHub:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd "Interactive Dashboard Development"
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### Step 2: Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv dashboard_env
.\dashboard_env\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Verify the data files

Ensure all four CSV files are present inside the `data/` directory.

### Step 5: Run the dashboard

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal. By default, Streamlit uses:

`http://localhost:8501`

## ☁️ Deployment

The application can be deployed using Streamlit Community Cloud.

1. Push the project to a GitHub repository.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Sign in and connect your GitHub account.
4. Create a new app and select the repository and branch.
5. Set the main file path to `app.py`.
6. Deploy the application.
7. Test the public dashboard URL and verify the charts and filters.

Ensure the CSV files and `requirements.txt` are committed to the repository if the deployed application depends on them.

## 📸 Screenshots and Demo

Add screenshots of the running dashboard to the `screenshots/` directory.

Suggested screenshots:

- Executive Overview with KPI cards
- Web Traffic & Acquisition page
- Customer Churn page
- Checkout A/B Test page
- Regional Market map
- Data Quality & Assumptions page

**Live Dashboard:** Add your deployed URL here after successful deployment.

**Demo Video:** Add your video link here if submitting a walkthrough instead of a live URL.

## 📦 Internship Deliverables

- [x] Interactive Streamlit dashboard implementation
- [x] KPI summary cards
- [x] Interactive filters
- [x] Responsive Plotly charts
- [x] Analysis of four datasets
- [x] Data cleaning and assumption documentation
- [ ] Public dashboard URL or video walkthrough
- [ ] Final screenshots and GitHub repository link

Update the remaining checklist items after completing deployment and submission.

## 🔮 Future Improvements

- Add statistical significance testing and confidence intervals for A/B experiments.
- Introduce configurable outlier detection and cleaning reports.
- Add automated data validation tests.
- Improve accessibility and mobile responsiveness.
- Add scheduled data refresh when a reliable updated data source becomes available.

## 👨‍💻 Author

**Arpit Singh Tomar**

B.Tech Computer Science and Engineering  
Workora Virtual Internship — Interactive Dashboard Development

## 📄 License and Data Disclaimer

This project was developed for educational and internship purposes. The supplied datasets are synthetic. Do not present the analysis as actual Workora customer, revenue, retention, or market performance.

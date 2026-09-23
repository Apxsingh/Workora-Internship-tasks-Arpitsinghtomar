# Customer Churn Analysis

Analysis of customer subscription data to identify patterns behind cancellations and compute key retention metrics — built as part of a Data Analytics virtual internship task.

## 📌 Objective

Calculate churn rate, Customer Lifetime Value (CLV), and Monthly Recurring Revenue (MRR) loss, and identify the key behavioral and contractual drivers of customer churn.

## 📂 Project Structure

```
customer-churn-analysis/
│
├── chrun_env        # Python Virtual Enviroment
│
├── data/
│   └── customer_churn_sample (1).csv        # Raw customer dataset
│
├── images 
│   └── Churn_rate_by_contract_type.png
│   └── Churn_rate_by_customer_tenure_months.png
│   └── Churn_rate_by_payment_methods.png
│   └── Correlation_Heatmap.png
│   └── Customer_churn_distribution.png
│   └── Monthly_charges_by_monthly_status.png
│   └── Tenure_months_distribution_by_churn_status.png
│
├── notebook        
│   └── Customer_Churn_Analysis.ipynb           # Main analysis notebook
│
├── report   # Final analytics report (submission deliverable)
│   └── Customer_Churn_Analysis_Report.pdf          # Final analytics report (submission deliverable)
│
├── .gitignore
│
├── README.md
│
├── requirements.txt
```

## 🧾 Dataset

15 customer records with the following attributes:

| Column | Description |
|---|---|
| `CustomerID` | Unique customer identifier |
| `Gender` | Customer gender |
| `Age` | Customer age |
| `TenureMonths` | Number of months as a subscriber |
| `SubscriptionType` | Basic / Pro / Enterprise |
| `MonthlyCharges` | Monthly subscription fee (₹) |
| `TotalCharges` | Total amount billed to date (₹) |
| `ContractType` | Month-to-Month / One Year / Two Year |
| `SupportTickets` | Number of support tickets raised |
| `PaymentMethod` | Credit Card / Debit Card / Bank Transfer / UPI |
| `Churn` | Yes / No |

No missing values or duplicate records were found during data cleaning.

## 🛠️ Tools & Libraries

- Python 3.11
- pandas, numpy
- matplotlib, seaborn
- Jupyter Notebook

## 🔍 Workflow

1. **Data Loading & Cleaning** – Loaded the dataset, checked shape, dtypes, missing values, and duplicates.
2. **Churn Flag Encoding** – Mapped `Churn` (Yes/No) to a binary `Churn_Flag` (1/0).
3. **Core Metrics** – Calculated baseline churn rate, MRR loss, and CLV.
4. **Segmentation** – Grouped churn rate by contract type, tenure, payment method, subscription type, and support tickets.
5. **Visualization** – Generated bar charts, boxplots, and a correlation heatmap.
6. **Driver Analysis** – Compared numeric feature averages (monthly charges, tenure, age) across churned vs. retained customers, and built a correlation matrix to rank behavioral drivers.
7. **Recommendations** – Translated findings into actionable retention strategies.

## 📊 Key Results

| Metric | Value |
|---|---|
| Total Customers | 15 |
| Churned Customers | 7 |
| **Churn Rate** | **46.67%** |
| Total MRR | ₹1,269.85 |
| **MRR Lost (churned customers)** | **₹409.93** (≈32.3% of total MRR) |
| Average Monthly Revenue | ₹84.66 |
| Average Customer Tenure | 18.8 months |
| **Estimated CLV** | **₹1,591.55** |

### Churn Rate by Segment

| Factor | Highest-Risk Group | Churn Rate |
|---|---|---|
| Contract Type | Month-to-Month | 100.00% |
| Payment Method | Debit Card | 100.00% |
| Support Tickets | 5 tickets | 100.00% |
| Subscription Type | Basic | 71.43% |

### Behavioral Drivers (Correlation with Churn)

- **Support Tickets:** r = 0.88 (strongest positive driver)
- **Tenure (Months):** r = -0.80
- **Age:** r = -0.73
- **Monthly Charges:** r = -0.59

Churned customers average **7.0 months** of tenure vs. **29.1 months** for retained customers, and pay **₹58.56/month** on average vs. **₹107.49/month** for retained customers.

## 💡 Key Recommendations

1. Convert Month-to-Month customers to annual plans through switch incentives.
2. Launch a proactive retention program targeting the first 90 days of the subscription.
3. Flag and prioritize customers who cross 3+ support tickets before they churn.
4. Investigate renewal friction on Debit Card and UPI payment rails.
5. Strengthen the Basic tier's value proposition and upgrade path to Pro.
6. Track CLV-to-CAC alongside churn to prioritize retention spend.

*(Full explanations for each recommendation are in the PDF report.)*

## 📦 Deliverable

`Customer_Churn_Analysis_Report.pdf` — a formatted analytics report containing the executive summary, dataset overview, retention metrics, segmentation charts, correlation analysis, and business recommendations, submitted as proof of task completion.

## ▶️ How to Run

```bash
pip install pandas numpy matplotlib seaborn jupyter 
jupyter notebook Customer_Churn_Analysis.ipynb
```

## ✍️ Author

**Arpit Singh Tomar**
B.Tech CSE, IPS College of Technology and Management, Gwalior
Data Analytics Virtual Internship by *WORKORA*
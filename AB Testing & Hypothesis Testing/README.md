# A/B Testing & Hypothesis Testing

## Project Overview

This project analyzes an A/B test for a website checkout process to determine whether Variant B performs better than Variant A in terms of user conversion rate.

The project follows a complete data analysis workflow, including data cleaning, exploratory data analysis, statistical hypothesis testing, confidence intervals, effect size analysis, visualization, and reporting.

## Objectives

- Compare conversion rates between Variant A and Variant B.
- Measure absolute and relative conversion lift.
- Perform statistical hypothesis testing to evaluate the difference between variants.
- Calculate confidence intervals for conversion rates and the difference between them.
- Analyze conversion performance across devices and traffic sources.
- Examine revenue and order value metrics.
- Generate visualizations and a PDF report with findings and recommendations.

## Dataset

**File:** `checkout_ab_test_v2.csv`

**Location:** `data/checkout_ab_test_v2.csv`

The dataset contains 1,200 website visitor records and the following columns:

| Column | Description |
|---|---|
| `VisitorID` | Unique identifier for each visitor |
| `Variant` | A/B test group assigned to the visitor |
| `Timestamp` | Date and time of the visitor's activity |
| `Device` | Device category used by the visitor |
| `TrafficSource` | Source through which the visitor arrived |
| `CheckoutStarted` | Whether the visitor started checkout |
| `Converted` | Whether the visitor completed a conversion |
| `OrderValueINR` | Order value in Indian rupees |

## Tools and Technologies

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Statsmodels

## Project Structure

```text
AB Testing & Hypothesis Testing/
│
├── data/
│   └── checkout_ab_test_v2.csv
│
├── notebook/
│   ├── AB_Testing_Hypothesis_Testing.ipynb
│   └── outputs/
│       ├── conversion_rates.png
│       ├── conversion_lift.png
│       ├── visitor_outcomes.png
│       └── ab_test_report.pdf
│
│
├── README.md
├── .gitignore
└── AB_Testing_env/
```

*Note: The notebook filename above is an example. Replace it with your actual filename if it differs.*

## Methodology

### 1. Data Cleaning and Validation

- Load the dataset using Pandas.
- Check missing values and duplicate records.
- Validate visitor identifiers and test variant labels.
- Convert timestamps into the correct datetime format.
- Encode conversion outcomes as binary values.

### 2. Exploratory Data Analysis

- Examine the distribution of visitors across variants.
- Calculate conversion counts and conversion rates.
- Explore device categories and traffic sources.
- Investigate order values and checkout behavior.

### 3. Hypothesis Testing

The analysis uses a significance level of **5% (α = 0.05)**.

**Null hypothesis (H₀):** The conversion rates of Variant A and Variant B are equal.

**Alternative hypothesis (H₁):** The conversion rates of Variant A and Variant B are different.

The analysis uses a two-proportion z-test and a chi-square test of independence to assess whether the observed conversion difference is statistically significant.

### 4. Confidence Intervals and Effect Size

- Calculate 95% confidence intervals for each variant's conversion rate.
- Estimate the confidence interval for the difference between conversion rates.
- Calculate absolute conversion lift and relative conversion lift.
- Estimate effect size using Cohen's h.
- Estimate the sample size required for a future experiment under the selected assumptions.

### 5. Segmentation and Revenue Analysis

Compare conversion performance across:

- Device categories
- Traffic sources
- Checkout behavior
- Order value and revenue metrics

Segment-level findings are treated as exploratory, especially when sample sizes are small or multiple comparisons are performed.

### 6. Visualization and Reporting

The notebook generates conversion charts, visitor outcome comparisons, and a PDF report summarizing the analysis and recommendations.

## Key Metrics

| Metric | Meaning |
|---|---|
| Conversion Rate | Conversions divided by visitors |
| Absolute Lift | Conversion rate of B minus conversion rate of A |
| Relative Lift | Absolute lift divided by conversion rate of A |
| P-value | Evidence against the null hypothesis |
| Confidence Interval | Plausible range for the estimated conversion rate or difference |
| Average Order Value | Average order value among orders with positive value |
| Revenue per Visitor | Total order value divided by the number of visitors |

## How to Run the Project

### Prerequisites

Install Python and create or activate the project's virtual environment.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd "AB Testing & Hypothesis Testing"
```

Replace the repository URL with your actual GitHub repository URL.

### 2. Create and activate a virtual environment (optional)

If you are creating a new environment:

```bash
python -m venv AB_Testing_env
```

On Windows PowerShell:

```powershell
.\AB_Testing_env\Scripts\Activate.ps1
```

If the environment already exists, activate it instead of creating another one.

### 3. Install dependencies

```bash
python -m pip install pandas numpy scipy statsmodels matplotlib seaborn jupyter ipykernel
```

### 4. Open Jupyter Notebook

```bash
jupyter notebook
```

Open the notebook inside the `notebook/` folder and execute the cells in order.

The notebook saves generated charts and the PDF report in `notebook/outputs/`.

## Interpreting the Results

The decision should be based on the observed conversion lift, the p-value, and the confidence interval for the difference between variants.

- If Variant B shows a statistically significant positive lift, consider a controlled rollout after checking revenue, costs, and other guardrail metrics.
- If Variant B shows a statistically significant negative lift, retain Variant A while investigating the result.
- If the difference is not statistically significant, do not conclude that the variants are equivalent. Consider the confidence interval, statistical power, and whether additional data is needed.

**Important:** The final recommendation must reflect the actual results produced by the notebook. No variant should be declared the winner before the statistical analysis is complete.

## Limitations

- The analysis assumes visitors were assigned to variants appropriately and independently.
- The dataset may not represent every real-world website visitor.
- Statistical significance does not automatically imply practical or business significance.
- Segment-level comparisons may have limited statistical power.
- A causal interpretation depends on the quality of the experiment design and data collection.

## Deliverables

- Jupyter Notebook containing the analysis
- Data cleaning and validation results
- Statistical hypothesis tests
- Conversion and lift visualizations
- Segment and revenue analysis
- PDF report with findings and recommendations
- Screenshots documenting the project

## Author

**Arpit Singh Tomar**

B.Tech Computer Science and Engineering  
Interests: Data Analytics, Machine Learning, and Software Development

---

*This project was completed as part of an internship-style data analytics project to demonstrate practical A/B testing and statistical hypothesis testing skills.*
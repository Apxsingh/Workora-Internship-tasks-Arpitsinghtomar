# Predictive Churn Analysis

## Project Overview

This project develops a machine learning system to predict customer churn using customer demographics, subscription details, billing information, and customer support activity.

The objective is to identify customers who are likely to leave a service so that businesses can take proactive retention measures.

The project was completed as part of the Workora internship tasks and demonstrates an end-to-end machine learning workflow, including data cleaning, preprocessing, model training, evaluation, and churn-risk prediction.

## Objectives

- Clean and validate customer data.
- Explore customer churn patterns.
- Encode categorical variables using One-Hot Encoding.
- Scale numerical features using MinMaxScaler.
- Train and compare Logistic Regression and Random Forest classifiers.
- Evaluate models using Accuracy, Precision, Recall, F1 Score, and ROC-AUC.
- Generate customer-level churn predictions and risk categories.
- Export the trained model and evaluation results.

## Dataset

**File:** `data/customer_churn_model_v2.csv`

The dataset contains 800 customer records and 13 columns.

### Features

| Feature | Description |
|---|---|
| CustomerID | Unique customer identifier |
| Age | Customer age |
| Region | Customer's region |
| TenureMonths | Duration of the customer's relationship |
| SubscriptionType | Subscription plan |
| MonthlyChargesINR | Monthly charges in INR |
| TotalChargesINR | Total charges in INR |
| ContractType | Type of customer contract |
| SupportTickets | Number of support tickets |
| LatePayments | Number of late payments |
| PaymentMethod | Customer's payment method |
| AutoPay | Whether automatic payment is enabled |
| Churn | Target variable indicating whether a customer churned |

### Dataset Summary

- Total records: 800
- Total original columns: 13
- Duplicate rows identified: 0
- Missing values identified: 0
- Customers who churned: 334 (41.75%)
- Customers who did not churn: 466 (58.25%)

`CustomerID` was excluded from model training because it is an identifier rather than a useful predictive feature.

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib

## Project Structure

```text
Predictive Churn Analysis/
│
├── data/
│   └── customer_churn_model_v2.csv
│
├── notebook/
│   ├── churn_analysis.ipynb
│   └── output/
│       ├── churn_risk_predictions.csv
│       ├── model_evaluation_metrics.csv
│       ├── model_evaluation_report.json
│       ├── best_churn_model.joblib
│       └── project_summary.txt
│
├── README.md
├── .gitignore
└── requirements.txt
```

The output directory may also contain saved ROC curves, confusion matrices, and other evaluation artifacts.

## Machine Learning Workflow

### 1. Data Cleaning

- Loaded and inspected the dataset.
- Checked missing values and duplicate records.
- Removed duplicate records if present.
- Removed rows without a valid target value if necessary.
- Removed the customer identifier from the feature set.
- Standardized target labels.

### 2. Feature Engineering and Preprocessing

The target variable was encoded as:

- `No` → 0
- `Yes` → 1

Numerical features were processed using median imputation and MinMax scaling. Categorical features were processed using most-frequent imputation and One-Hot Encoding.

A Scikit-learn `ColumnTransformer` and `Pipeline` were used to combine preprocessing with model training and help prevent data leakage.

### 3. Train-Test Split

The dataset was divided using an 80/20 split with stratification.

- Training samples: 640
- Testing samples: 160
- Random state: 42

### 4. Model Training

Two classification algorithms were trained:

- Logistic Regression
- Random Forest Classifier

Class weighting was used to help account for the difference in the number of churn and non-churn customers.

## Model Evaluation

The models were evaluated on the held-out test set.

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.669 | 0.583 | 0.731 | 0.649 | 0.681 |
| Random Forest | 0.637 | 0.557 | 0.657 | 0.603 | 0.658 |

### Best Performing Model

**Logistic Regression** achieved the highest ROC-AUC score among the two evaluated models.

Its main test-set results were:

- Accuracy: 66.9%
- Churn precision: 58.3%
- Churn recall: 73.1%
- F1 Score: 0.649
- ROC-AUC: 0.681

These results represent an initial baseline. Further feature engineering, threshold tuning, cross-validation, and hyperparameter optimization may improve performance.

## Churn-Risk Predictions

The project exports customer-level predictions to:

`notebook/output/churn_risk_predictions.csv`

The output includes:

- CustomerID
- ActualChurn
- PredictedChurn
- ChurnProbability
- RiskCategory

Risk categories are assigned using illustrative probability thresholds:

- **High:** Probability ≥ 0.70
- **Medium:** Probability ≥ 0.40 and < 0.70
- **Low:** Probability < 0.40

These categories are intended for demonstration and should be validated against business needs before practical use. Model probabilities are not necessarily calibrated probabilities of real-world churn.

## Installation and Usage

### Prerequisites

- Python 3.10 or newer
- pip
- Jupyter Notebook or Visual Studio Code with the Jupyter extension

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd "Predictive Churn Analysis"
```

Replace the placeholder repository URL with your actual GitHub repository URL.

### 2. Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv PCA_env
.\PCA_env\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can install packages using the environment's Python executable directly.

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Open the Notebook

Open `notebook/churn_analysis.ipynb` in VS Code or Jupyter Notebook.

Select the Python kernel associated with your project environment and run the notebook cells in order.

Ensure the dataset is available at `data/customer_churn_model_v2.csv`.

### 5. Review the Outputs

After successful execution, review the generated files inside `notebook/output/`.

## Future Improvements

- Perform cross-validation and hyperparameter tuning.
- Compare additional algorithms such as Gradient Boosting.
- Improve probability calibration and optimize the classification threshold.
- Analyze the factors associated with churn.
- Add an interactive dashboard using Streamlit.
- Deploy the model as an API.
- Test the model on new customer records.

## Limitations

- The model is trained on a dataset of 800 records.
- The evaluation results are based on one train-test split.
- The results may not generalize to other customer populations.
- Risk categories use illustrative thresholds and require business validation.
- Churn predictions should support, rather than automatically determine, customer retention decisions.

## Author

**Arpit Singh Tomar**

B.Tech Computer Science and Engineering

GitHub: [Apxsingh](https://github.com/Apxsingh)

## License

Choose an appropriate open-source license before distributing this project. If no license has been added, the repository remains subject to the default copyright rules.

---

*Developed for educational and internship purposes as a demonstration of an end-to-end customer churn prediction workflow.*
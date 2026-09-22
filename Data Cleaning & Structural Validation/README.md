

# Data Cleaning & Structural Validation

## 1. Import Libraries

## 2. Load Dataset

## 3. Initial Data Inspection
   - head()
   - shape
   - columns
   - info()
   - describe()

## 4. Missing Value Analysis

## 5. Duplicate Record Analysis

## 6. Data Type Validation

## 7. Numerical Data Validation
   - Age
   - Tenure
   - Monthly Charges
   - Total Charges
   - Support Tickets

## 8. Categorical Data Validation
   - Gender
   - Subscription Type
   - Contract Type
   - Payment Method
   - Churn

## 9. Data Cleaning
   - Standardize column names
   - Remove whitespace
   - Standardize categorical strings

## 10. Customer ID Validation

## 11. Charge Consistency Validation

## 12. Final Validation

## 13. Export Cleaned Dataset

## 14. Data Cleaning Summary

The dataset initially contained 15 records and 11 columns. A complete data-quality inspection was performed using Python and Pandas.

No missing values were detected, so no imputation or deletion of records was required. No duplicate rows or duplicate Customer IDs were found. Numerical columns were checked for invalid negative values, and no invalid values were identified.

Categorical columns were inspected for consistency, and column names were standardized using snake_case. Leading and trailing whitespace was removed from categorical values.

The relationship between total_charges, tenure_months, and monthly_charges was also validated. No significant charge mismatches were found.

After cleaning and structural validation, the dataset contains 15 rows and 11 columns and was exported as cleaned_customer_data.csv.

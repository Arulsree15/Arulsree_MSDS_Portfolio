# Employee Attrition in Remote Work Environments

## Author
Arulsree Mozhi, TS

## Date
February 15, 2025

## Project Overview
This project predicts employee attrition in remote work environments using HR analytics data. It provides insights for HR teams to proactively manage employee satisfaction and reduce turnover.

## Dataset
- `WA_Fn-UseC_-HR-Employee-Attrition.csv` (IBM HR Analytics Employee Attrition & Performance)
- 1,470 employee records with 35 attributes

## Installation & Requirements
```bash
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl joblib
```

## Usage

1. Load and preprocess the dataset:
python data_preprocessing.py

2. Train baseline Logistic Regression model:
python train_model.py

3. Evaluate model performance:
python evaluate_model.py

4. Save and load model for future predictions:
import joblib
model = joblib.load('attrition_model.pkl')

## Evaluation Metrics

Accuracy

Precision

Recall

F1-score

Confusion Matrix

ROC AUC Score

## Key Insights

Low job satisfaction and younger age correlate with higher attrition.

Employees in Sales and R&D are more prone to leave.

Distance from home affects attrition even in remote settings.

## Future Enhancements

Test advanced ML models (Random Forest, Gradient Boosting)

Improve recall to reduce false negatives

Deploy model for proactive HR monitoring
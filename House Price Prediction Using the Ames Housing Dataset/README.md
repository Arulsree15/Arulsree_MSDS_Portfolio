# House Price Prediction

## Project Overview
This project focuses on predicting **house prices** using the **Ames Housing Dataset**. The analysis includes comprehensive **data preprocessing, feature engineering, model building, and evaluation**. The goal is to provide actionable insights into factors influencing house prices and develop predictive models to assist buyers, sellers, and real estate professionals.

The project applies **Linear Regression, Random Forest, and XGBoost** to predict sale prices and evaluates model performance using standard regression metrics.

---

## Data Preparation

### 1. Data Cleaning
- **Lot Frontage:** Missing values imputed with median of respective **Neighbourhood**.
- **Categorical Variables:** Missing values in features like `GarageType`, `GarageFinish`, `GarageQual`, `GarageCond`, `MasVnrType` replaced with `'None'`.
- **MasVnrArea:** Missing values replaced with `0`.
- **Dropped Columns:** `PID`, `Alley`, `PoolQC`, `Fence`, `MiscFeature` due to irrelevance or high missing values.

### 2. Feature Engineering
- **Total Square Footage (`TotalSF`)**: Sum of `GrLivArea`, `1stFlrSF`, and `2ndFlrSF`.
- **House Age (`HouseAge`)**: Difference between `YrSold` and `YearBuilt`.
- **Log Transformation:** `SalePrice` transformed using `np.log1p` to reduce skewness.
- **One-Hot Encoding:** Categorical variables converted to numerical format.

---

## Model Building and Evaluation

### 1. Model Selection
- **Linear Regression** – simple and interpretable baseline.
- **Random Forest** – captures non-linear interactions.
- **XGBoost** – high-performance model for complex datasets.

### 2. Data Splitting and Scaling
- **Train/Test Split:** 80% training, 20% testing.
- **Feature Scaling:** StandardScaler applied to normalize features for Linear Regression.

### 3. Training & Evaluation
- **Metrics Used:**
  - **Mean Squared Error (MSE):** 1,436,316,419.94
  - **Mean Absolute Error (MAE):** 16,462.33
  - **R-Squared (R²):** 0.8209

- **Visualizations:**
  - Actual vs Predicted SalePrice scatter plot
  - Residual plot to check model assumptions

**Interpretation:**  
R² indicates the model explains ~82% of variance in house prices. Residual plots suggest potential non-linear patterns or heteroscedasticity, indicating that more complex models or additional feature engineering could further improve performance.

---

## Recommendations
1. **Explore More Complex Models:** Random Forest, Gradient Boosting (XGBoost), or ElasticNet.  
2. **Advanced Feature Engineering:** Interaction terms or external economic variables.  
3. **Cross-Validation & Regularization:** Prevent overfitting with Lasso/Ridge or k-fold CV.  
4. **Further Data Cleaning:** Examine outliers and potential errors for better model performance.

---

## Learning Objectives
- Identify key factors affecting house prices.
- Apply machine learning for real estate valuation.
- Gain practical experience with regression modeling.
- Improve predictive accuracy through preprocessing and feature engineering.

---

## Risks and Ethical Considerations
- **Data Quality:** Handle missing or inconsistent data.
- **Bias and Fairness:** Mitigate historical biases in housing valuations.
- **Overfitting:** Apply cross-validation and regularization.

---

## Tools & Technologies
- Python 3.10+  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  
- XGBoost  
- Jupyter Notebook  

---

## Usage
1. Clone the repository:

```bash
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction
```
2. Install dependencies:
pip install -r requirements.txt

3. Open Jupyter notebooks to explore analysis, visualizations, and model training.

References

Kozue. (2023). Ames Housing Dataset. Kaggle. Retrieved March 22, 2025, from https://www.kaggle.com/datasets/shashanknecrothapa/ames-housing-dataset
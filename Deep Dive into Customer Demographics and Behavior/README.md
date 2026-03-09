# Deep Dive into Customer Demographics and Behavior

## Author
Arulsree Mozhi, TS

## Date
August 06, 2024

## Dataset
Customer Personality Analysis  
[https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)

## Description
This project analyzes customer demographics and purchase behavior to understand the influence of family composition and age on purchase frequency (`Recency`) and complaints (`Complain`). It uses exploratory data analysis, histograms, PMF, CDF, scatter plots, t-tests, and regression analysis.

## Requirements
- Python 3.x
- Pandas
- NumPy
- SciPy
- Matplotlib
- Seaborn
- Statsmodels
- IPython (for displaying tables)

## Files
- `marketing_campaign.csv` : Dataset  
- `customer_analysis.py` : Python script for cleaning, visualization, and analysis  

## How to Run
1. Place `marketing_campaign.csv` in the working directory.  
2. Run `customer_analysis.py` in a Python environment.  
3. Visualizations will be displayed for histograms, PMF, CDF, scatter plots, and distribution analysis.  
4. Regression and t-test results will print in the console.

## Notes
- Outliers in `Recency` and `Year_Birth` are removed using the IQR method.  
- CDF and PMF plots are used to compare households with and without children.  
- Regression results suggest weak predictive power of selected demographic variables.
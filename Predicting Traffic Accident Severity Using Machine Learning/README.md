# Predicting Traffic Accident Severity Using Machine Learning

**Author:** Arulsree Mozhi, Thangaraj Santhakumar  
**Institution:** Bellevue University  
**Course:** DSC680 – Applied Data Science  
**Instructor:** Prof. Amirfarrokh Iranitalab  
**Project:** Term Project 2 – Milestone 3  
**Date:** February 15, 2026  

---

## Project Overview

Road traffic accidents continue to result in significant loss of life, injuries, and economic damage despite improvements in vehicle safety technologies and traffic management systems. Modern transportation technologies such as Advanced Driver Assistance Systems (ADAS) and autonomous vehicles rely on predictive analytics to improve driving safety.

This project develops a **machine learning framework to predict traffic accident severity** using historical crash data and environmental conditions. By identifying patterns associated with severe crashes, the model can support safer driving systems, transportation planning, and proactive risk assessment.

---

## Dataset

The project uses the **US Accidents Dataset (2016–Present)** obtained from Kaggle.  
The dataset contains millions of accident records collected from traffic sensors, public agencies, and incident reports across the United States.

Dataset source:
https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents

Key variables used in this project include:

- Accident Severity
- Start Time
- Temperature
- Humidity
- Visibility
- Wind Speed
- Precipitation
- Weather Conditions
- Traffic Signal Presence
- Junction Indicators
- Crossing Indicators

A **sample dataset** is included in this repository for demonstration.

---

## Project Workflow

The project follows a standard **end-to-end data science workflow**:

1. Data loading and sampling
2. Data preprocessing and feature engineering
3. Exploratory data analysis and visualization
4. Model development using multiple machine learning algorithms
5. Model evaluation and performance comparison
6. Interpretation of feature importance

---

## Machine Learning Models

Three supervised classification models were implemented and compared:

- Logistic Regression
- Random Forest
- Gradient Boosting

The dataset was split into **training and testing sets**, and model performance was evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score

---

## Model Performance

| Model               | Accuracy | Precision | Recall | F1 Score |
|---------------------|----------|-----------|--------|----------|
| Logistic Regression | 0.8265   | 0.6832    | 0.8265 | 0.7481   |
| Random Forest       | 0.8131   | 0.7210    | 0.8131 | 0.7505   |
| Gradient Boosting   | 0.8264   | 0.7211    | 0.8264 | 0.7485   |

Overall, **Logistic Regression and Gradient Boosting achieved the highest accuracy (~82%)** while Random Forest provided strong interpretability through feature importance analysis.

---

## Key Findings

The analysis revealed that accident severity is influenced by a combination of **environmental, temporal, and roadway factors**, including:

- Reduced visibility
- Adverse weather conditions
- Time of day
- Roadway infrastructure features

Feature importance analysis identified **visibility, weather conditions, time of day, and traffic signals** as some of the most influential predictors.

These insights demonstrate the potential for integrating predictive models into **ADAS and intelligent transportation systems**.

---

## Repository Structure
traffic-accident-severity-prediction
│
├── notebook.ipynb
├── dataset_sample.csv
│
├── figures
│ ├── figure1.png
│ ├── figure2.png
│ ├── figure3.png
│ ├── figure4.png
│ ├── figure5.png
│ └── figure6.png
│
├── report.pdf
├── requirements.txt
└── README.md


---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Future Work

Future improvements could include:

- Incorporating real-time traffic and vehicle telemetry data
- Using deep learning models for improved prediction
- Developing dynamic accident risk maps
- Integrating the model into real-time driver assistance systems

---

## References

Kaggle. (2023). US accidents (2016–present) dataset.  
https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents

Moosavi, S., Samavatian, M. H., Parthasarathy, S., & Ramnath, R. (2019).  
*A countrywide traffic accident dataset.*  
Proceedings of the 4th ACM SIGSPATIAL International Workshop on Data Science for Intelligent Transportation Systems.

National Highway Traffic Safety Administration. (2023).  
Traffic Safety Facts Annual Report.  
U.S. Department of Transportation.

---

## Author

**Arulsree Mozhi**  
Master of Science in Data Science  
Bellevue University
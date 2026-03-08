# Artificial Intelligence and the Changing IT Workforce

**Authors:** Arulsree Mozhi, Thangaraj Santhakumar  
**Date:** March 6, 2026  

---

## Project Overview

The rapid integration of **Artificial Intelligence (AI)** into IT environments is reshaping workforce requirements. Organizations face challenges in understanding which IT roles are most likely to adopt AI tools and how workforce experience levels influence AI integration.  

This project analyzes AI adoption patterns among IT professionals and developers to support **workforce planning, skill development, and strategic AI implementation**.

---

## Dataset

- **Source:** Stack Overflow Developer Survey 2023  
- **Scope:** Global responses from professional and hobbyist developers  
- **Key Variables:**
  - `DevType` – Primary development role  
  - `YearsCode` – Coding experience  
  - `Age`  
  - `Industry`  
  - `LanguageHaveWorkedWith`  
  - AI-related usage indicators: `AISelect`, `AIToolCurrentlyMostlyAI`, `UsesAI`  

Data preprocessing included:
- Splitting multi-role entries in `DevType`  
- Mapping age categories into groups  
- Converting coding experience to numeric format  
- Creating a binary AI usage variable (`UsesAI`)  
- Encoding categorical features for machine learning

---

## Methods

- Exploratory Data Analysis (EDA) to visualize AI adoption across:
  - Developer roles
  - Experience levels
  - Age groups
  - Programming languages
  - Industries
- Seven visualizations created for trend analysis (Figures 1–7)
- Machine learning modeling:
  - Random Forest classifier to predict AI adoption
  - Features: developer role, coding experience, age group, industry
  - Evaluation metrics: Accuracy, Precision, Recall, F1-score
- Classification report generated to assess predictive performance

---

## Key Results

- Overall AI adoption among developers: **77.8%**  
- Highest adoption among: data scientists, ML engineers, full-stack developers  
- Years of coding experience correlates with AI usage  
- AI users predominantly use **Python, JavaScript, and SQL**  
- Industries with highest adoption: software development, IT consulting, research-intensive sectors  
- Developer perception of AI impact: mostly **positive**

- Random Forest classifier performance: **Accuracy = 83%**  
- High precision and recall for AI users; moderate performance for non-users  

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

## Future Applications

- Longitudinal trend analysis in AI adoption  
- Regional and industry-specific adoption patterns  
- Predictive modeling of skill gaps for emerging AI roles  
- Integration with organizational workforce planning systems  

---

## Recommendations

- Prioritize AI adoption in high-impact roles  
- Provide targeted training for mid-level developers  
- Monitor adoption among older or less experienced cohorts  
- Encourage cross-functional exposure to AI tools  

---

## Implementation Plan

- Map current workforce roles to AI adoption likelihood  
- Deploy targeted upskilling programs  
- Monitor AI tool utilization and integrate feedback  
- Use predictive models for recruitment and training optimization  

---

## Ethical Considerations

- Avoid bias in AI deployment  
- Ensure equitable access to AI-enhancing tools  
- Safeguard employee autonomy  
- Maintain transparency in AI adoption objectives and workforce implications

---

## References

- Stack Overflow. (2023). *Stack Overflow Developer Survey.* [Link](https://insights.stackoverflow.com/survey)  
- World Economic Forum. (2023). *The Future of Jobs Report 2023.* [Link](https://www.weforum.org/reports/the-future-of-jobs-report-2023)  
- Python Software Foundation. (2026). *Python Language Reference.* [Link](https://www.python.org/)
# Childcare Affordability Challenges in the United States

## Project Overview
This project analyzes **childcare costs across U.S. states** using the National Database of Childcare Prices (NDCP). The analysis focuses on **median costs by age group** (infants, toddlers, preschoolers) and compares them to **median household income**. Python and Tableau were used to clean, aggregate, and visualize the data, highlighting geographic disparities, historical trends, and affordability challenges.

The goal is to inform **policy decisions, parental guidance, and advocacy efforts** to improve childcare affordability.

---

## Key Findings
- **Infant care** is consistently the most expensive, with **California, Massachusetts, and New York** leading in cost.
- Midwest and Southern states generally have **lower childcare costs**.
- Many states show **gradual cost increases**, while some remain stable due to subsidies or lower demand.
- In high-cost states, **infant care can consume over 25% of median household income**, far exceeding the 7% affordability benchmark.
- Data quality is high; minimal missing data exists, but **inflation adjustment is recommended** for longitudinal analysis.

---

## Assumptions
- `MCInfant`, `MCToddler`, `MCPreschool` represent **full-time care costs**.
- Study year reflects the **data collection year** accurately.
- State-level aggregated data represents **overall state trends**.
- Socioeconomic indicators are **current and reliable**.
- Minimal missing data does **not skew results**.

---

## Target Audience
- Policymakers & Government Officials  
- Parents & Caregivers  
- Nonprofits & Advocacy Groups  
- Researchers & Academics  

---

## Mediums Included
1. **Interactive Dashboard** – dynamic exploration of state-level cost trends with filters for state, age group, and year.  
2. **Analytical Report** – structured PDF detailing methodology and policy implications.  
3. **Explainer Video** – 3–5 minute overview for parents and advocacy groups.

---

## Design Decisions
- **Choropleth Map** – highlight geographic disparities  
- **Bar Charts** – compare costs as % of income  
- **Trend Lines** – show historical changes  
- **KPI Cards** – emphasize quick highlights  
- Clear labels, legends, and tooltips to avoid misinterpretation

---

## Ethical Considerations
- Removed incomplete records and aggregated county-level data to state-level.  
- Data is **publicly available from U.S. Department of Labor**, no privacy violations.  
- Choropleth maps could exaggerate differences; mitigated by **affordability metrics**.  
- Documented assumptions, transparent filtering, and verified data accuracy.  

---

## Policy Recommendations
1. **Enhance Childcare Subsidies** – Expand federal and state support to cover more families, aligning with the **7% income benchmark**.  
2. **Invest in Infant Care Infrastructure** – Prioritize funding for public/subsidized infant care centers to reduce high cost burden and improve access.  

---

## Tools & Technologies
- Python 3.10+  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Tableau  

---

## Usage
1. Clone the repository:

```bash
git clone https://github.com/your-username/childcare-affordability.git
cd childcare-affordability
```
2. Install dependencies:
pip install -r requirements.txt

3. Open Jupyter notebooks or Tableau dashboards to explore visualizations and analysis.

---

References

U.S. Department of Labor. (n.d.). National Database of Childcare Prices. Retrieved from https://www.dol.gov/agencies/wb/topics/childcare
# Mental Health Impacts of Social Media Usage among Young Adults

## Authors
Arulsree Mozhi, Thangaraj Santhakumar  
05/24/2024

## Overview
This project investigates the relationship between social media usage and mental health outcomes among young adults. Using three datasets (Pew Research Center, NIMH Surveys, Twitter interactions), we analyze patterns, predict outcomes, and visualize key insights.

## Required R Packages
- tidyverse
- caret
- ggplot2
- cowplot
- gridExtra
- RColorBrewer
- ggpubr
- corrplot
- heatmaply
- ggrepel
- knitr
- kableExtra
- lubridate
- readxl
- writexl
- cluster
- forcats

## How to Run
1. Place datasets in the `data/` folder.  
2. Run `data_cleaning.R` to clean and save datasets to `cleaned_data/`.  
3. Run `analysis_pew.R`, `analysis_nimh.R`, and `analysis_twitter.R` to generate visualizations and tables.  
4. Check `outputs/` for plots and tables.  
5. Compile the report in `report/` for final submission.

## Description of Analyses
- **Social Media Engagement:** Clustering and predictive modeling of Pew data.  
- **Demographic Classification:** Decision trees, logistic regression, and clustering of NIMH data.  
- **Twitter Interaction:** Clustering and time series analysis of engagement metrics.  

## Notes
- Data may include missing values and needs cleaning before analysis.  
- Ensure R packages are installed using `install.packages("package_name")`.  
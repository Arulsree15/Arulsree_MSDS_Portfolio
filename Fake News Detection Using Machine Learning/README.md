# Fake News Detection Using Machine Learning

**Authors:** Arulsree Mozhi, Thangaraj Santhakumar  
**Date:** January 15, 2026  

---

## Project Overview

Fake news spreads rapidly online and can significantly influence public opinion, political decisions, and individual behavior. Traditional fact-checking methods cannot keep up with the speed at which information circulates on the internet. 

This project applies **machine learning** to detect fake news in online articles. The goal is to assist media outlets, social media platforms, and readers in quickly identifying misleading information. 

Key objectives:

- Differentiate real and fake news articles
- Evaluate machine learning model performance
- Examine textual, sentiment, and social engagement characteristics
- Provide actionable insights to reduce online misinformation

---

## Dataset

This project uses three publicly available datasets:

1. **LIAR dataset:** Political statements rated on a six-point truthfulness scale  
2. **Fake and Real News dataset (Kaggle):** News articles labeled as real or fake  
3. **FakeNewsNet dataset:** Articles with social context and engagement metrics  

All datasets are **publicly available** and contain no personally identifiable information.

---

## Data Preparation

- Removed duplicates and irrelevant records  
- Tokenized text and filtered stop words  
- Calculated sentiment scores using TextBlob  
- Generated readability metrics  
- Extracted TF-IDF features and n-grams  
- Handled missing or inconsistent labels  

Key features used:

- Full article text  
- Real/Fake labels  
- Sentiment polarity  
- Readability scores  
- Social engagement metrics

---

## Methods

- Exploratory Data Analysis (EDA) with word clouds and TF-IDF analysis  
- Feature engineering: TF-IDF vectorization, n-grams, sentiment, readability, social context  
- Machine Learning models implemented:  
  - Logistic Regression  
  - Random Forest  
  - Support Vector Machines  
  - Gradient Boosting (XGBoost)  
  - Simple neural network / LSTM (optional)  
- Model evaluation metrics: Accuracy, Precision, Recall, F1-Score, Confusion Matrices  
- Visualization of sentiment distribution, feature importance, and textual patterns  

---

## Key Results

- Random Forest and Gradient Boosting achieved **highest accuracy**  
- Classification performance improves when combining textual and social context features  
- Feature importance highlights influential words and sentiment polarity  
- Final Random Forest performance on dataset:

| Class        | Precision | Recall | F1-score | Support |
|--------------|-----------|--------|----------|--------|
| FAKE         | 1.00      | 1.00   | 1.00     | 4733   |
| REAL         | 1.00      | 1.00   | 1.00     | 4247   |
| Accuracy     | -         | -      | 1.00     | 8980   |
| Macro Avg    | 1.00      | 1.00   | 1.00     | 8980   |
| Weighted Avg | 1.00      | 1.00   | 1.00     | 8980   |

---

## Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- TextBlob  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  

---

## Future Work

- Deploy models via API for continuous monitoring  
- Incorporate real-time social media streams  
- Implement hybrid systems combining automated detection with human review  
- Extend models to multiple languages and domains  

---

## Ethical Considerations

- Avoid labeling legitimate viewpoints as fake  
- Ensure transparency in prediction methods  
- Human editorial review should complement automated systems  
- Maintain accountability and clear communication of limitations

---

## References

- Kaggle. (2020). Fake and Real News Dataset. [Link](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)  
- Shu, K., Wang, S., & Liu, H. (2019). *Beyond news contents: The role of social context for fake news detection.* WSDM 2019. [PDF](https://www.cs.emory.edu/~kshu5/files/wsdm_2019_fake_news.pdf)  
- Wang, W. Y. (2017). *“Liar, liar pants on fire”: A new benchmark dataset for fake news detection.* arXiv:1705.00648
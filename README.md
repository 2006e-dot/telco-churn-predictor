# 🔮 Telco Customer Churn Predictor

**[🔴 Try the Live Web App Here!](https://telco-churn-predictor-24gdq46qf4ptnurmhsyaum.streamlit.app/)**

## Overview
This is an end-to-end Machine Learning web application designed to predict the likelihood of a customer canceling their subscription (churning). By analyzing customer demographics, account information, and subscribed services, this tool allows businesses to identify at-risk customers in real-time and take proactive steps to retain them.

## The Business Problem
Customer churn is a critical metric for any subscription-based business. Acquiring a new customer is significantly more expensive than retaining an existing one. This project acts as an early-warning system, acting to plug the "leaky bucket" of revenue loss by highlighting exactly which customers require targeted retention offers.

## Technical Stack
* **Language:** Python
* **Data Processing & Engineering:** Pandas, Scikit-Learn
* **Machine Learning:** Logistic Regression (Baseline Model)
* **Web Framework & Deployment:** Streamlit Community Cloud

## Machine Learning Pipeline (Version 1.0)
This baseline model was built with a strict, leak-proof pipeline:
1. **Data Cleaning:** Handled missing values strategically using business logic rather than blind imputation (e.g., treating blank tenure charges as $0 for brand-new customers).
2. **Feature Engineering:** Applied One-Hot Encoding for categorical text variables.
3. **Data Scaling:** Implemented `StandardScaler` strictly on continuous numeric variables to prevent data leakage between train/test sets.
4. **Model Training:** Trained a baseline Logistic Regression classifier, focusing heavily on evaluating **Recall** to ensure the maximum number of actual churning customers are caught by the model.
5. ## 📊 Model Performance (Baseline)

- Accuracy: 82.18%
- Churn Recall: 60%
- Precision (Churn): 69%
⚠️ The model prioritizes overall accuracy but misses ~40% of churners.
This highlights the need for imbalance handling and recall optimization in future versions.

## Future Enhancements (Version 2.0 Roadmap)
While the current model establishes a strong baseline, future iterations will focus on combating the natural class imbalance of the Telco dataset:
* Transitioning from linear models to advanced tree-based algorithms (Random Forest, XGBoost, AdaBoost) to capture complex, non-linear patterns.
* Implementing SMOTE (Synthetic Minority Over-sampling Technique) to balance the training data.
* Tuning hyper-parameters specifically to maximize the recall of the minority class (churners).

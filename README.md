# 🔮 Telco Customer Churn Predictor

**[🔴 Try the Live Web App Here!](https://telco-churn-predictor-na5optlbiwndbmwfbbpeyd.streamlit.app/)**

---

## 📌 Overview

This is an end-to-end Machine Learning web application designed to predict customer churn. By analyzing demographics, services, and account details, the model identifies customers who are likely to leave, enabling proactive retention strategies.

---

## 💼 Business Problem

Customer churn directly impacts revenue. Retaining existing customers is significantly cheaper than acquiring new ones. This system acts as an early-warning tool to help businesses target high-risk customers and reduce churn.

---

## 🛠️ Technical Stack

* **Language:** Python
* **Data Processing:** Pandas, Scikit-Learn
* **Machine Learning:** XGBoost (Final Model), Logistic Regression (Baseline)
* **Deployment:** Streamlit Community Cloud

---

## ⚙️ Machine Learning Pipeline

1. **Data Cleaning**

   * Handled missing values using business logic
   * Converted `TotalCharges` to numeric and removed invalid entries

2. **Feature Engineering**

   * Applied One-Hot Encoding for categorical features
   * Ensured consistency between training and inference

3. **Feature Scaling**

   * Used `StandardScaler` on numeric features (`tenure`, `MonthlyCharges`, `TotalCharges`)

4. **Model Training**

   * Started with Logistic Regression (baseline)
   * Upgraded to **XGBoost** for better performance
   * Handled class imbalance using `scale_pos_weight`

5. **Evaluation Strategy**

   * Focused on **Recall (Churn class)** instead of just accuracy
   * Used Precision, Recall, and F1-score for evaluation

---

## 📊 Model Performance (Final - XGBoost)

* **Accuracy:** ~77%
* **Recall (Churn):** ~83% 🔥
* **Precision (Churn):** ~54%
* **F1-score (Churn):** ~0.65

✅ The model prioritizes **high recall**, ensuring most churn customers are correctly identified.
⚠️ Slightly lower precision indicates some false positives, which is acceptable in churn prediction.

---

## 🔍 Key Insight

> "In churn prediction, missing a churn customer is more costly than incorrectly flagging a loyal one."

---

## 🚀 Future Enhancements

* Threshold tuning for better precision-recall balance
* Feature importance & SHAP explainability
* Trying CatBoost for categorical optimization
* Building a full ML pipeline using `ColumnTransformer`
* Adding database integration for real-time predictions

---

## 🌐 Web App Features

* Clean and interactive UI
* Real-time churn prediction
* Input validation for realistic values
* Probability-based risk interpretation

---

##  Conclusion

This project demonstrates a complete ML lifecycle:

* Data preprocessing
* Model selection and tuning
* Handling class imbalance
* Deployment using Streamlit

The final model is optimized for **business impact rather than raw accuracy**, making it practical for real-world use.

---

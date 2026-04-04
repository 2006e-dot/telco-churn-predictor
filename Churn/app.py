import streamlit as st
import pandas as pd
import joblib

model = joblib.load("logistic_model.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("model_columns.pkl")

st.set_page_config(layout="wide")
st.title("Telco Customer Churn Predictor 🔮")
st.markdown("Provide the following details to check the customer's churn risk:")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Demographics")
    gender = st.selectbox("Gender", ["Female", "Male"])
    SeniorCitizen = st.selectbox("Senior Citizen?", [0, 1])
    Partner = st.selectbox("Partner?", ["No", "Yes"])
    Dependents = st.selectbox("Dependents?", ["No", "Yes"])

with col2:
    st.subheader("Services Subscribed")
    PhoneService = st.selectbox("Phone Service?", ["No", "Yes"])
    MultipleLines = st.selectbox("Multiple Lines?", ["No", "Yes"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online Security?", ["No", "Yes"])
    OnlineBackup = st.selectbox("Online Backup?", ["No", "Yes"])
    DeviceProtection = st.selectbox("Device Protection?", ["No", "Yes"])
    TechSupport = st.selectbox("Tech Support?", ["No", "Yes"])
    StreamingTV = st.selectbox("Streaming TV?", ["No", "Yes"])
    StreamingMovies = st.selectbox("Streaming Movies?", ["No", "Yes"])

with col3:
    st.subheader("Account Details")
    tenure = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=12)
    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing?", ["No", "Yes"])
    PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    MonthlyCharges = st.number_input("Monthly Charges ($)", min_value=0.0, value=50.0)
    TotalCharges = st.number_input("Total Charges ($)", min_value=0.0, value=600.0)

st.divider()

def yes_no(val):
    return 1 if val == "Yes" else 0

if st.button("Predict Churn Risk", use_container_width=True):

    raw_input = {
        'tenure': tenure,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges,
        'SeniorCitizen': SeniorCitizen,
        'Partner': yes_no(Partner),
        'Dependents': yes_no(Dependents),
        'PhoneService': yes_no(PhoneService),
        'MultipleLines': yes_no(MultipleLines),
        'OnlineSecurity': yes_no(OnlineSecurity),
        'OnlineBackup': yes_no(OnlineBackup),
        'DeviceProtection': yes_no(DeviceProtection),
        'TechSupport': yes_no(TechSupport),
        'StreamingTV': yes_no(StreamingTV),
        'StreamingMovies': yes_no(StreamingMovies),
        'PaperlessBilling': yes_no(PaperlessBilling),
        
        'gender_' + gender + '_True': 1,
        'Contract_' + Contract + '_True': 1,
        'InternetService_' + InternetService + '_True': 1,
        'PaymentMethod_' + PaymentMethod + '_True': 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    input_df[num_cols] = scaler.transform(input_df[num_cols])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error(f"🚨 **High Risk of Churn!** (Probability: {probability:.1%})")
        st.write("Action: Consider a targeted retention offer.")
    else:
        st.success(f"✅ **Customer is safe.** (Churn Probability: {probability:.1%})")
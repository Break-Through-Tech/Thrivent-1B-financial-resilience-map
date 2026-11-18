import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("outputs/final_model.joblib")


# Page title and description
st.title("Household Financial Resilience Predictor")

st.write(
    "Enter the household information below to estimate "
    "the probability of financial fragility."
)


# Input fields for household information
age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

hh_size = st.number_input(
    "Household Size",
    min_value=1,
    max_value=12,
    value=2
)

income = st.selectbox(
    "Household Income",
    [
        "Select",
        "Less than $10,000",
        "$10,000 to $24,999",
        "$25,000 to $49,999",
        "$50,000 to $74,999",
        "$75,000 to $99,999",
        "$100,000 to $149,999",
        "$150,000 or more"
    ]
)

education = st.selectbox(
    "Education Level",
    [
        "Select",
        "No high school diploma or GED",
        "High school graduate (high school diploma or the equivalent GED)",
        "Some college or Associate's degree",
        "Bachelor's degree",
        "Master's degree or higher"
    ]
)

employment = st.selectbox(
    "Employment Status",
    [
        "Select",
        "Working full-time",
        "Working part-time",
        "Not working"
    ]
)

housing_ownership = st.selectbox(
    "Housing/Ownership",
    [
        "Select",
        "Own your home with a mortgage or loan",
        "Own your home free and clear (without a mortgage or loan)",
        "Pay rent",
        "Neither own nor pay rent"
    ]
)

medical_debt = st.selectbox(
    "Medical Debt",
    [
        "Select",
        "Yes",
        "No"
    ]
)

income_stability = st.selectbox(
    "Income Stability",
    [
        "Select",
        "Roughly the same amount each month",
        "Occasionally varies from month to month",
        "Varies quite often from month to month"
    ]
)

financial_situation = st.selectbox(
    "Current Financial Situation",
    [
        "Select",
        "Finding it difficult to get by",
        "Just getting by",
        "Doing okay",
        "Living comfortably"
    ]
)

emergency_savings = st.selectbox(
    "Emergency Savings",
    [
        "Select",
        "Yes",
        "No"
    ]
)

food_sufficiency = st.selectbox(
    "Food Sufficiency",
    [
        "Select",
        "Enough of the kinds of food we wanted to eat",
        "Enough, but not always the kinds of food we wanted to eat",
        "Sometimes not enough to eat",
        "Often not enough to eat"
    ]
)

credit_confidence = st.selectbox(
    "Credit Access/Confidence",
    [
        "Select",
        "Don't know",
        "Very confident",
        "Somewhat confident",
        "Not confident"
    ]
)


# Predict button and display result
if st.button("Predict"):
    if (
        employment == "Select" 
        or education == "Select" 
        or income == "Select" 
        or income_stability == "Select"
        or financial_situation == "Select" 
        or emergency_savings == "Select" 
        or food_sufficiency == "Select" 
        or credit_confidence == "Select"
        or housing_ownership == "Select"
        or medical_debt == "Select"
    ):
        st.error("Please complete all required fields.")

    else:
        input_data = pd.DataFrame({
            "ppage": [age],
            "pphhsize": [hh_size],
            "ppinc7": [income],
            "ppeduc5": [education],
            "ppemploy": [employment],
            "GH1": [housing_ownership],
            "E2B": [medical_debt],
            "I9": [income_stability],
            "B2": [financial_situation],
            "EF1": [emergency_savings],
            "FD3": [food_sufficiency],
            "A6": [credit_confidence]
        })

        probability = model.predict_proba(input_data)[0][1]

        st.success(
            f"Estimated probability of financial fragility: "
            f"{probability:.1%}"
        )
import streamlit as st
import pandas as pd
import joblib

def page_prediction_body():
    st.title("House Price Prediction")
    st.info("Input details below to predict the house price.")

    # Load model
    model = joblib.load('outputs/trained_model.pkl')

    # User inputs
    GrLivArea = st.number_input("Above-grade Living Area (sq ft)", min_value=300, max_value=6000, value=1500)
    OverallQual = st.slider("Overall Quality", min_value=1, max_value=10, value=5)
    GarageArea = st.number_input("Garage Area (sq ft)", min_value=0, max_value=1500, value=500)
    TotalBsmtSF = st.number_input("Total Basement Area (sq ft)", min_value=0, max_value=3000, value=800)

    # Predict button
    if st.button("Predict Price"):
        input_df = pd.DataFrame([[GrLivArea, OverallQual, GarageArea, TotalBsmtSF]],
                                columns=['GrLivArea', 'OverallQual', 'GarageArea', 'TotalBsmtSF'])
        prediction = model.predict(input_df)[0]
        st.success(f"✅ Predicted House Price: ${prediction:,.2f}")

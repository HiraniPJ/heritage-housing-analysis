import streamlit as st
import pandas as pd
import joblib

def page_prediction_body():
    st.title("House Price Prediction")
    st.info("Input details below to predict the house price.")

    # Load model
    model = joblib.load('outputs/trained_model.pkl')

    st.header("Enter House Features")

    # User inputs
    gr_liv_area = st.number_input("Above-ground Living Area (sq ft)", min_value=300, max_value=6000, value=1500)
    overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
    garage_area = st.number_input("Garage Area (sq ft)", min_value=0, max_value=1500, value=500)
    total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", min_value=0, max_value=6000, value=800)
    
    # Predict button
    if st.button("Predict Price"):
        input_df = pd.DataFrame([[GrLivArea, OverallQual, GarageArea, TotalBsmtSF]],
                                columns=['GrLivArea', 'OverallQual', 'GarageArea', 'TotalBsmtSF'])
        prediction = model.predict(input_df)[0]
        st.success(f"✅ Predicted House Price: ${prediction:,.2f}")

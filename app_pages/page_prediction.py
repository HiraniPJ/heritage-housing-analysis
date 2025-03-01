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
    garage_area = st.number_input("Garage Area (sq ft)", min_value=0, max_value=1500, value=500)
    overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
    total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", min_value=0, max_value=6000, value=800)
    
    # Prepare input data for prediction
    input_features = pd.DataFrame({
        'GrLivArea': [gr_liv_area],
        'GarageArea':[garage_area],
        'OverallQual': [overall_qual],
        'TotalBsmtSF': [total_bsmt_sf]
    })

    # Predict button
    if st.button("Predict House Price"):
        prediction = model.predict(input_features)
        predicted_price = np.round(prediction[0], 2)
        st.success(f"✅ Predicted House Price: ${prediction:,.2f}")

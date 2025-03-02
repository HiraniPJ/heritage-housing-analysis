import streamlit as st
import pandas as pd
import joblib

def page_prediction_body():
    st.title("House Price Prediction")
    st.info("Enter details below to predict the house price.")

    # Load model
    model = joblib.load('outputs/trained_model.pkl')

    st.header("Enter House Features")

    # Prepare input data for prediction
    selected_features = ["GrLivArea", "GarageArea", "TotalBsmtSF", "OverallQual"]

    #input files for the users to enter values
    user_inputs = {}
    for feature in selected_features:
        user_inputs[feature] = st.number_input(f"Enter {feature}:", value=0)

    # User inputs into dataframe
    input_df = pd.DataFrame([user_inputs])

    # column order matches the model's training
    input_df = input_df[selected_features]

    # Predict button
    if st.button("Predict House Price"):
        prediction = model.predict(input_df)
        st.success(f"✅ Predicted House Price: ${prediction[0]:,.2f}")

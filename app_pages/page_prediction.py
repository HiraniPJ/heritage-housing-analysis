import streamlit as st
import pandas as pd
import joblib
import os

def page_prediction_body():
    st.title("House Price Prediction (What-If)")
    st.info("Enter details below to estimate the sale price.")

    # 1) Load model
    model_path = "outputs/trained_model.pkl"
    if not os.path.exists(model_path):
        st.error("Trained model not found at outputs/trained_model.pkl. Please run the modeling notebook.")
        return

    obj = joblib.load(model_path)
    # Unpack (model, selected_features)
    if isinstance(obj, tuple) and len(obj) == 2:
        model, selected_features = obj
    else:
        # Fallback
        model = obj
        selected_features = ["GrLivArea", "GarageArea", "TotalBsmtSF", "OverallQual"]

    st.caption(f"Model expects features (in order): {', '.join(selected_features)}")

    # 2) Collect user inputs
    inputs = {} 
    for feat in selected_features:
        if feat in ["GrLivArea", "GarageArea", "TotalBsmtSF"]:
            inputs[feat] = st.number_input(feat, min_value=0, step=10, value=1500 if feat=="GrLivArea" else 500)
        elif feat == "OverallQual":
            inputs[feat] = st.slider("OverallQual (1-10)", 1, 10, 6)
        else:
            # integers for these numeric square-foot features
            inputs[feat] = st.number_input(feat, value=0)

    # User inputs into dataframe
    X = pd.DataFrame([[inputs[f] for f in selected_features]], columns=selected_features)


    # 3) Predict
    if st.button("Predict House Price"):
        try:
            prediction = float(model.predict(X)[0])
            st.success(f"✅ Predicted House Price: **${prediction:,.2f}**")
        except Exception as e:
            st.error(f"Prediction failed: {e}")
            st.code(f"Input columns: {list(X.columns)}\nExpected: {selected_features}")
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

def page_prediction_body():
    st.title("House Price Prediction (What-If)")
    st.info("Enter details below to estimate the sale price.")

    # 1) Load model
    pkl_path = Path('outputs/trained_model.pkl')
    if not pkl_path.exists():
        st.error(f"Trained model not found at {pkl_path}. Please run the modelling notebook to generate it.")
        return

    try:
        loaded = joblib.load(pkl_path)
    except Exception as e:
        st.error(f"Could not load the trained model: {e}")
        return
  
    # Unpack (model, selected_features)
    if isinstance(loaded, tuple) and len(loaded) == 2:
        model, selected_features = loaded
    else:
        # Fallback
        model = loaded
        selected_features = ["GrLivArea", "GarageArea", "TotalBsmtSF", "OverallQual"]


    # 2) Collect user inputs
    st.subheader("Enter House Features")
    values = {}
    #default setup
    defaults = {
        "GrLivArea": 1500,     # sq ft
        "GarageArea": 500,     # sq ft
        "TotalBsmtSF": 800,    # sq ft
        "OverallQual": 6       # 1–10
    } 

    for feat in selected_features:
        if feat == "OverallQual":
            values[feat] = st.number_input(feat, min_value=1, max_value=10, value=int(defaults.get(feat, 6)), step=1)
    else:
            # integers for these numeric square-foot features
            values[feat] = st.number_input(feat, min_value=0, value=int(defaults.get(feat, 0)), step=50)

    # User inputs into dataframe
    input_df = pd.DataFrame([values])[selected_features]


    # 3) Predict
    if st.button("Predict House Price"):
        try:
            prediction = float(model.predict(input_df)[0])
        except Exception as e:
            st.error(f"Prediction failed: {e}")
            return
        st.success(f"✅ Predicted House Price: ${prediction:,.2f}")

    #  Debugging
    with st.expander("Details (for debugging)"):
        st.write("Features used by the model (order matters):", selected_features)
        st.dataframe(input_df)
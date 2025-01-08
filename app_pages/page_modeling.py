import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def page_modeling_body():
    """
    Displays the Modeling and Evaluation page.

    This page provides insights into the machine learning model performance, including visualizations and data tables.

    Returns:
        None
    """

    st.title("Modeling and Evaluation")
    st.info("This page provides insights into the machine learning model performance.")

    # Model Performance Metrics
    st.header("Model Performance Metrics")

    # Display the Actual vs Predicted Comparison Plot
    try:
        st.image("outputs/model_actual_vs_predicted.png", caption="Actual vs Predicted Comparison", use_container_width=True)
    except FileNotFoundError:
        st.error("Actual vs Predicted Comparison plot not found. Please ensure it exists at 'outputs/model_actual_vs_predicted.png'.")

    # Load and Display Predictions CSV
    predictions_path = "outputs/inherited_houses_with_predictions.csv"
    try:
        predictions_df = pd.read_csv(predictions_path)
        st.subheader("Predictions Overview")
        st.dataframe(predictions_df)
    except FileNotFoundError:
        st.error(f"Predictions file not found: {predictions_path}")

    # Display Additional Insights (if applicable)
    st.subheader("Additional Insights")
    st.write("This section can include other model metrics, such as RMSE, MAE, or R-squared values, if calculated.")

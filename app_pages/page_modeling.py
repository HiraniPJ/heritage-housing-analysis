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

    try:
        with open("outputs/model_metrics.json", "r") as f:
            metrics = json.load(f)

        # Model Performance Metrics
        st.subheader("Model Performance Metrics")
        st.write(f"**R² Score:** {metrics['R2 Score']}")
        st.write(f"**Mean Absolute Error (MAE):** {metrics['Mean Absolute Error (MAE)']}")
        st.write(f"**Root Mean Squared Error (RMSE):** {metrics['Root Mean Squared Error (RMSE)']}")

        # Interpretation
        st.markdown("#### **Interpretation of Results:**")
        if metrics["R2 Score"] >= 0.75:
            st.success("✅ The model has a strong predictive ability.")
        elif metrics["R2 Score"] >= 0.5:
            st.warning("⚠️ The model has moderate predictive power but can be improved.")
        else:
            st.error("❌ The model does not generalize well. Consider improving feature selection or hyperparameter tuning.")

    except FileNotFoundError:
        st.error("Model evaluation results not found. Please run model training first.")
    
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json


def page_modeling_body():
    """
    Displays the Modeling and Evaluation page.

    This page provides insights into the machine learning model performance, including visualizations and data tables.

    Returns:
        None
    """

    st.title("Modeling and Evaluation")
    st.info("This page provides insights into the machine learning model performance.")

    # Defines the path for model evaluation metrics
    metrics_file = "outputs/model_metrics.json"

    try:
        with open(metrics_file, "r") as f:
            metrics = json.load(f)
        
        # Model Performance Metrics
        st.subheader("Model Performance Metrics")

        if "Train R²" in metrics:
            st.write(f"**Train R² Score:** {metrics['Train R²']}")
        else:
            st.warning(" `Train R² Score` not found.")

        if "Test R²" in metrics:
            test_r2 = metrics["Test R²"]
            st.write(f"**Test R² Score:** {test_r2}")
        else:
            st.warning(" `Test R² Score` not found.")
            test_r2 = None  # Ensure test_r2 is defined

        if "Cross-Validation Mean R²" in metrics:
            st.write(f"**Cross-Validation Mean R²:** {metrics['Cross-Validation Mean R²']} (± {metrics['Cross-Validation Std Dev']})")
        else:
            st.warning(" `Cross-Validation Mean R²` not found.")

        if "Mean Absolute Error (MAE)" in metrics:
            st.write(f"**Mean Absolute Error (MAE):** {metrics['Mean Absolute Error (MAE)']}")
        else:
            st.warning(" `Mean Absolute Error (MAE)` not found.")

        if "Root Mean Squared Error (RMSE)" in metrics:
            st.write(f"**Root Mean Squared Error (RMSE):** {metrics['Root Mean Squared Error (RMSE)']}")
        else:
            st.warning(" `Root Mean Squared Error (RMSE)` not found.")

        # Interpretation of Results
        st.markdown("#### **Interpretation of Results:**")
        if test_r2 is not None:
            if test_r2 >= 0.75:
                st.success("✅ The model has a strong predictive ability.")
            elif test_r2 >= 0.5:
                st.warning(" The model has moderate predictive power but can be improved.")
            else:
                st.error("❌ The model does not generalize well. Consider improving feature selection or hyperparameter tuning.")
        else:
            st.error("❌ Test R² Score is missing. Unable to assess model generalization.")

    except FileNotFoundError:
        st.error(f"❌ Model evaluation results not found at `{metrics_file}`. Please run model training first.")
    except json.JSONDecodeError:
        st.error(f"❌ Error decoding `{metrics_file}`. Ensure it is correctly formatted.")

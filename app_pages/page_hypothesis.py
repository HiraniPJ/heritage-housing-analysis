import streamlit as st

def page_hypothesis_body():
    st.title("Objectives, Hypotheses & Validation")
    st.info("Why I made these assumptions and how I tested them.")

    st.subheader("Objective O1: Trustable Predictions")
    st.markdown("""
    **Hypothesis (H1):** A simple, transparent linear model can generalize well on Ames data.  
    **Validation:** 80/20 split + 5-fold cross-validation. 
       """)
    st.success("**Outcome:** Test R² **0.791**, CV mean **0.735** ⇒ **Met**.")
 

    st.subheader("Objective O2: Explain Value Drivers")
    st.markdown("""
    **Hypothesis (H2):** Larger living area and higher overall quality are the main price drivers; basement and garage add value with smaller effects.  
    **Validation:** Correlations, scatter plots, and linear coefficients.
    """)
    st.success("**Outcome:** **Supported** – `GrLivArea` and `OverallQual` dominate; `TotalBsmtSF` and `GarageArea` contribute with diminishing returns.")


    st.subheader("Objective O3: Enable Scenario Testing")
    st.markdown("""
    **Hypothesis (H3):** A streamlined input form aligned to the model’s features enables reliable “what-if” analysis.  
    **Validation:** App inputs map exactly to the model features; predictions returned instantly.
    """)
    st.success("**Outcome:** **Supported** – Prediction page implemented and validated.")


    st.caption("See the Modeling & Evaluation page for metrics and diagnostics, and the Data Visualization page for supporting plots.")
import streamlit as st

def page_hypothesis_body():
    st.title("Project Hypotheses and Validation")
    st.info("This page outlines and validates the project hypotheses.")

    st.write("### Hypothesis 1")
    st.markdown("Visual insights from data help identify key patterns in housing prices.")
    st.success("Validated through correlation heatmaps and box plots.")

    st.write("### Hypothesis 2")
    st.markdown("Machine learning can predict house prices with high accuracy.")
    st.success("Validated through the evaluation of model metrics.")

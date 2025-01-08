import streamlit as st

def page_summary_body():
    st.title("Project Summary")
    st.info("This page provides a summary of the project, objectives, and achievements.")

    st.write("### Key Business Requirements")
    st.markdown("""
    1. Visualize housing data to identify patterns and trends.
    2. Build a predictive model to estimate house prices.
    3. Provide actionable insights for stakeholders.
    """)
    st.success("All business requirements have been successfully addressed.")

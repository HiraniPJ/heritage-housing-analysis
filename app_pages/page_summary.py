import streamlit as st

def page_summary_body():
    st.title("Project Summary")
    st.info("This page provides a summary of the project, objectives, and achievements.")

    st.write("### Key Business Requirements")
    st.markdown("""

    1. **Data Exploration & Visualization:** Identify and showcase the relationships between property features and sale prices through various plots and charts.

    2. **Price Prediction:** Develop a machine learning model capable of predicting house prices with a high degree of accuracy.

    3. **Interactive Dashboard:** Provide an easy-to-use web application for real-time property price estimation and data exploration.

    4. **Actionable Insights:** Offer strategic recommendations for property improvement based on key influencing factors.
    """)
    st.success("All business requirements have been successfully addressed.")

import streamlit as st

def page_summary_body():
    st.title("Project Summary")
    st.info("This page provides a summary of the project, objectives, and achievements.")

    st.write("### Key Client's Business Requirements")
    st.markdown("""

    1. **Data Exploration & Visualization:** Clearly show how core features (e.g., living area, quality, basement, garage) affect **SalePrice** through various plots and charts.

    2. **Price Prediction:** Provide reliable, explainable estimates for new houses with transparent metrics (R², MAE, RMSE).

    3. **Interactive Dashboard:** Let the client run **what-if** scenarios in real time.

    4. **Actionable Insights:** Turn findings into practical recommendations (pricing & renovation priorities).

    ### Delivery Summary

    - A **Linear Regression** model trained on Ames data with **Test R² = 0.791** and **5-fold CV mean R² = 0.735**.
    - **Exploration** pages with static and interactive visuals.
    - A **Prediction** page that accepts user inputs aligned to the model’s features.
    - **Insights** highlighting the biggest value drivers (living area and quality) and secondary ones (basement and garage).

    """)
    st.success("All business requirements have been successfully addressed.")

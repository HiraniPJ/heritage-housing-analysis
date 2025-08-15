import streamlit as st
import json
import os

def _fmt_float(x, nd=3):
    return f"{x:.{nd}f}" if isinstance(x, (int, float)) else "—"

def _fmt_money(x):
    return f"${x:,.0f}" if isinstance(x, (int, float)) else "—"

def page_modeling_body():
    """
    Displays the Modeling and Evaluation page.

    This page provides insights into the machine learning model performance, including visualizations and data tables.

    Returns:
        None
    """

    st.title("Modeling and Evaluation")
    st.info("This page summarizes how the model performs and how confidently you can use its predictions.")

    # 1)Load Metrics -------
    metrics_file = "outputs/model_metrics.json"
    if not os.path.exists(metrics_file):
        st.error(f"❌ Model evaluation results not found at `{metrics_file}`. Please run model training first.")
        return

    try:
        with open(metrics_file, "r") as f:
            m = json.load(f)
    except json.JSONDecodeError:
        st.error(f"❌ Error decoding `{metrics_file}`. Ensure it is valid JSON.")
        return

    #Read Keys
    train_r2 = m.get("Train R²", m.get("Train R2"))
    test_r2  = m.get("Test R²",  m.get("Test R2"))
    cv_mean  = m.get("Cross-Validation Mean R²", m.get("CV Mean R²"))
    cv_std   = m.get("Cross-Validation Std Dev", m.get("CV Std"))

    mae      = m.get("Mean Absolute Error (MAE)", m.get("MAE"))
    rmse     = m.get("Root Mean Squared Error (RMSE)", m.get("RMSE"))


    # 2) Model Performance Metrics -------------
    st.subheader("Model Performance Metrics")
    c1, c2, c3 = st.columns(3)
    c1.metric("Test R²", _fmt_float(test_r2))
    c2.metric("MAE", _fmt_money(mae))
    c3.metric("RMSE", _fmt_money(rmse))

    # Secondary metrics
    st.caption(
        f"Train R²: {_fmt_float(train_r2)}  •  "
        f"5-Fold CV Mean R²: {_fmt_float(cv_mean)}  (± {_fmt_float(cv_std)})"
    )

    # 3) Interpretation of Results ---------------
    st.markdown("#### **Interpretation of Results:**")
    if isinstance(test_r2, (int, float)):
        if test_r2 >= 0.75:
            st.success("✅ **Strong generalization** on unseen homes in Ames. Good basis for pricing ‘what-if’ scenarios.")
        elif test_r2 >= 0.50:
            st.warning(" ⚠️ **Moderate performance**. Consider adding features or tuning to improve accuracy.")
        else:
            st.error("❌ **Weak generalization**. Revisit feature selection and model choice.")
    else:
        st.error("❌ Test R² Score is missing. Unable to assess model generalization.")
    
    with st.expander("What do these metrics mean?"):
        st.markdown("""
        - A Test R² of ~0.79 indicates the model explains a large share of price variance on unseen homes.
        - MAE (~$25k) and RMSE (~$40k) set realistic error bounds for planning and negotiation.
        - CV mean R² close to Test R² with low variance suggests **robust generalization**.
        """)

    # 4) Diagnostic plots -------------
    st.subheader("Diagnostic Plots")
    plots = {
        "Actual vs Predicted (Test Set)": "outputs/model_actual_vs_predicted.png",
        "Residuals Plot": "outputs/residual_plot.png",
        "Cross-Validation Score Distribution": "outputs/cv_score_distribution.png",
    }

    found_any = False
    for label, path in plots.items():
        st.markdown(f"**{label}**")
        if os.path.exists(path):
            st.image(path, use_container_width=True)
            found_any =  True
        else:
            st.info(f"ℹ️ Not found at `{path}`(generate & save it in the notebook if you want it shown here).")

    if not found_any:
        st.caption("No plots found yet. Save them from the notebook into `outputs/` to display here.")

    # 5) Download Metrics (evidence) ---------
    with open(metrics_file, "rb") as f:
        st.download_button(
            label="Download model_metrics.json",
            data=f.read(),
            file_name="model_metrics.json",
            mime="application/json"
        )
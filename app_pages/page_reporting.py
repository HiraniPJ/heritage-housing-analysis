import streamlit as st

def page_reporting_body():
    st.title("Feedback and Reporting")
    st.info("This page allows users to provide feedback and report issues.")

    st.subheader("Feedback Form")
    rating = st.radio("Rate your experience:", ["Excellent", "Good", "Average", "Poor"])
    comments = st.text_area("Comments:")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")

    st.subheader("Report an Issue")
    issue = st.text_area("Describe the issue:")
    if st.button("Submit Issue"):
        st.success("Your issue has been reported. Thank you!")

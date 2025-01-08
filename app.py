import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page_summary import page_summary_body
from app_pages.page_data_visualization import page_data_visualization_body
from app_pages.page_modeling import page_modeling_body
from app_pages.page_data_loading import page_data_loading_body
from app_pages.page_hypothesis import page_hypothesis_body
from app_pages.page_reporting import page_reporting_body

# Create an instance of the app
app = MultiPage(app_name="Heritage Housing Analysis")

# Add pages
app.add_page("Summary", page_summary_body)
app.add_page("Data Loading", page_data_loading_body)
app.add_page("Data Visualization", page_data_visualization_body)
app.add_page("Modeling and Evaluation", page_modeling_body)
app.add_page("Hypothesis and Validation", page_hypothesis_body)
app.add_page("Feedback / Reporting", page_reporting_body)

# Run the app
app.run()

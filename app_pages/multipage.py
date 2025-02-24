import streamlit as st

from page_summary import page_summary_body
from page_data_loading import page_data_loading_body
from page_data_visualization import page_data_visualization_body
from page_hypothesis import page_hypothesis_body
from page_modeling import page_modeling_body
from page_prediction import page_prediction_body
from page_reporting import page_reporting_body

class MultiPage:
    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name
        st.set_page_config(page_title=self.app_name, page_icon="🏠")

    def add_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})

    def run(self):
        st.sidebar.title(self.app_name)
        page = st.sidebar.radio("Navigation", self.pages, format_func=lambda page: page["title"])
        page["function"]()

# multipage app instance
app = MultiPage("Heritage Housing Analysis")

# Pages to the app
app.add_page("Project Summary", page_summary_body)
app.add_page("Data Loading", page_data_loading_body)
app.add_page("Data Visualization", page_data_visualization_body)
app.add_page("Hypothesis Validation", page_hypothesis_body)
app.add_page("Modeling and Evaluation", page_modeling_body)
app.add_page("House Price Prediction", page_prediction_body)
app.add_page("Feedback and Reporting", page_reporting_body)
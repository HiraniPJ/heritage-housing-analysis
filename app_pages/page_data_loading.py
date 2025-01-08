import streamlit as st
import pandas as pd

def page_data_loading_body():
    st.title("Data Loading and Overview")
    st.info("This page loads and provides an overview of the dataset.")

    # Load datasets
    data_path = "data/house-price-20211124T154130Z-001/house-price"
    try:
        house_prices_df = pd.read_csv(f"{data_path}/house_prices_records.csv")
        inherited_houses_df = pd.read_csv(f"{data_path}/inherited_houses.csv")
        st.write("### House Prices Dataset")
        st.dataframe(house_prices_df.head())
        st.write("### Inherited Houses Dataset")
        st.dataframe(inherited_houses_df.head())
    except FileNotFoundError:
        st.error(f"Data files not found in {data_path}.")

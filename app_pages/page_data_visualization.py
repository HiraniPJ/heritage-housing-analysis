import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px

def page_data_visualization_body():
    st.title("Data Visualization")
    st.info("This page provides visual insights into the dataset.")

    output_dir = "outputs/data_visualization"

    # Correlation Heatmap
    st.header("Correlation Heatmap")
    heatmap_path = f"{output_dir}/correlation_heatmap.png"
    try:
        heatmap_image = Image.open(heatmap_path)
        st.image(heatmap_image, caption="Correlation Heatmap", use_container_width=True)
    except FileNotFoundError:
        st.error(f"Correlation Heatmap not found. Please ensure it exists at {heatmap_path}.")


    # Box Plots for Key Features
    st.header("Box Plots for Key Features")
    boxplot_files = {
        "GrLivArea vs SalePrice": f"{output_dir}/GrLivArea_vs_SalePrice.png",
        "OverallQual vs SalePrice": f"{output_dir}/OverallQual_vs_SalePrice.png",
        "GarageArea vs SalePrice": f"{output_dir}/GarageArea_vs_SalePrice.png"
    }

    for title, path in boxplot_files.items():
        st.subheader(title)
        try:
            boxplot_image = Image.open(path)
            st.image(boxplot_image, caption=title, use_container_width=True)
        except FileNotFoundError:
            st.error(f"{title} not found. Please ensure it exists at {path}.")
    
    # Load dataset for interactive charts
    data_path = "data/house_prices_records.csv"
    try:
        house_prices_df = pd.read_csv(data_path)
    except FileNotFoundError:
        st.error(f"Error: {data_path} not found.")
        return   

    # Interactive Sale Price Distribution
    st.header("Sale Price Distribution (Interactive)")
    fig_hist = px.histogram(
        house_prices_df,
        x="SalePrice",
        nbins=50,
        title="Distribution of Sale Prices"
    )
    st.plotly_chart(fig_hist)

    #Interactive Living Area vs. Sale Price
    st.header("Living Area vs Sale Price (Interactive)")
    fig_scatter_living = px.scatter(
        house_prices_df,
        x="GrLivArea",
        y="SalePrice",
        color="OverallQual",
        size="GarageArea",
        hover_data=["YearBuilt"],
        title="Living Area vs Sale Price (Colored by Overall Quality)"
    )
    st.plotly_chart(fig_scatter_living)

    #Interactive Garage Area vs. Sale Price
    st.header("Garage Area vs Sale Price (Interactive)")
    fig_scatter_garage = px.scatter(
        house_prices_df,
        x="GarageArea",
        y="SalePrice",
        color="OverallQual",
        size="GrLivArea",
        hover_data=["YearBuilt"],
        title="Garage Area vs Sale Price (Colored by Overall Quality)"
    )
    st.plotly_chart(fig_scatter_garage)

    # Summary Statistics
    st.header("Summary Statistics")
    st.write(house_prices_df.describe())
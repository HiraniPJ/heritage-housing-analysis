import streamlit as st
from PIL import Image

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


    # Box Plots
    st.header("Box Plots")
    boxplot_files = {
        "GrLivArea vs SalePrice": f"{output_dir}/GrLivArea_vs_SalePrice.png",
        "OverallQual vs SalePrice": f"{output_dir}/OverallQual_vs_SalePrice.png",
        "GarageArea vs SalePrice": f"{output_dir}/GarageArea_vs_SalePrice.png"
    }
    for title, path in boxplot_files.items():
        try:
            st.image(Image.open(path), caption=title, use_container_width=True)
        except FileNotFoundError:
            st.error(f"{title} not found at {path}.")

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

    # Distribution Plots for Numeric Features
    st.header("Distribution Plots for Numeric Features")
    distribution_files = {
        "SalePrice Distribution": f"{output_dir}/saleprice_distribution.png",
        "GrLivArea Distribution": f"{output_dir}/GrLivArea_distribution.png",
        "GarageArea Distribution": f"{output_dir}/GarageArea_distribution.png",
        "TotalBsmtSF Distribution": f"{output_dir}/TotalBsmtSF_distribution.png"
    }

    for title, path in distribution_files.items():
        st.subheader(title)
        try:
            dist_image = Image.open(path)
            st.image(dist_image, caption=title, use_container_width=True)
        except FileNotFoundError:
            st.error(f"{title} not found. Please ensure it exists at {path}.")


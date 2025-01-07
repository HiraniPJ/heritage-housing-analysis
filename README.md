# Heritage Housing Analysis

![Banner](readme_images/banner.png)

---

## Table of Contents

1. [Introduction](#introduction)
2. [How to Use This Repo](#how-to-use-this-repo)
3. [Dataset Content](#dataset-content)
4. [Business Requirements](#business-requirements)
5. [Hypothesis and Validation](#hypothesis-and-validation)
6. [The Rationale for Business Requirements Mapping](#the-rationale-for-business-requirements-mapping)
7. [Machine Learning Business Case](#machine-learning-business-case)
8. [Dashboard Design](#dashboard-design)
9. [Unfixed Bugs](#unfixed-bugs)
10. [Deployment](#deployment)
11. [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
12. [Credits](#credits)
13. [Acknowledgements](#acknowledgements)

---

## Introduction

The **Heritage Housing Analysis** project is designed to assist a client who has inherited four houses in Ames, Iowa. The primary goal is to help the client make data-driven decisions by predicting the sale prices of these houses using advanced machine learning techniques. The project also aims to provide a detailed analysis of how various housing features influence sale prices through visualizations and insights. Finally, an interactive web application will be developed to allow users to explore the data and make real-time predictions.

The project leverages data science methodologies and tools to analyze, predict, and visualize the housing market trends in Ames, Iowa. It provides a comprehensive solution that combines statistical analysis, machine learning, and user-friendly dashboards.

---

## How to Use This Repo

This repository is structured to enable seamless collaboration and deployment. Follow these steps to get started:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_REPO.git
   ```

2. **Set up your environment**:
   Log into your cloud IDE or local environment.

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Access Jupyter Notebooks**:
   Open the `jupyter_notebooks` directory and select `Notebook_Template.ipynb` to start exploring the project.

5. **Run the Streamlit dashboard locally**:
   Launch the dashboard by running the following command:
   ```bash
   streamlit run app/app.py
   ```

6. **Deploy to Heroku**:
   Follow the deployment steps outlined in the [Deployment](#deployment) section to make the application accessible online.

---

## Dataset Content

The dataset contains detailed records of housing features and their respective sale prices in Ames, Iowa. It includes attributes such as floor area, garage size, basement area, and other factors that influence property value. The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data).

### Key Features

| Variable        | Description                                  | Units         |
|------------------|----------------------------------------------|---------------|
| `GrLivArea`     | Above-grade living area square feet          | 334 - 5642    |
| `OverallQual`   | Overall material and finish quality          | 1 - 10        |
| `GarageArea`    | Garage size in square feet                   | 0 - 1418      |
| `YearBuilt`     | Original construction year                   | 1872 - 2010   |
| `SalePrice`     | Final sale price of the property             | 34900 - 755000|

Additional datasets:
- `house_prices_records.csv`: Contains records of various housing attributes and their sale prices.
- `inherited_houses.csv`: Details of the four inherited houses for price prediction.

---

## Business Requirements

The project addresses the following key business requirements:

1. **Explore and visualize how house attributes correlate with sale prices**:
   - The client wants to understand which features significantly impact property prices.
   - Visualizations such as scatter plots and heatmaps will provide these insights.

2. **Predict the sale prices of the inherited houses and other properties in Ames**:
   - A machine learning regression model will be built to generate accurate predictions.

3. **Develop an interactive dashboard for visualization and predictions**:
   - The dashboard will allow users to input property details and get real-time price predictions, along with interactive charts for data exploration.

---

## Hypothesis and Validation

### Hypothesis 1
- **Hypothesis**: Larger houses with higher quality materials and finishes sell for higher prices.
- **Validation**: Use correlation analysis and scatter plots to evaluate the relationship between `GrLivArea`, `OverallQual`, and `SalePrice`.

### Hypothesis 2
- **Hypothesis**: Properties with larger garage areas and better conditions contribute positively to sale prices.
- **Validation**: Perform regression analysis to measure the impact of `GarageArea` and `GarageFinish` on `SalePrice`.

### Hypothesis 3
- **Hypothesis**: Older houses may sell for less unless remodeled.
- **Validation**: Analyze the relationship between `YearBuilt`, `YearRemodAdd`, and `SalePrice` using visualizations.

---

## The Rationale for Business Requirements Mapping

### Business Requirement 1: Data Visualization
- Generate heatmaps to highlight correlations between features and sale prices.
- Use scatter plots for visualizing relationships between individual features like `GrLivArea`, `OverallQual`, and `SalePrice`.

### Business Requirement 2: Machine Learning Prediction
- Develop a regression model to predict house prices.
- Evaluate the model’s performance using R² and Mean Squared Error (MSE).

### Business Requirement 3: Interactive Dashboard
- Create an intuitive dashboard using Streamlit.
- Include sections for data exploration, real-time predictions, and model evaluation.

---

## Machine Learning Business Case

- **Objective**: Provide accurate sale price predictions for the inherited properties and any house in Ames.
- **Problem Statement**: Predicting house prices is challenging due to the diverse factors affecting property values.
- **Model Type**: Supervised regression model trained on labeled data.
- **Success Metrics**:
  - Achieve an R² score of 0.75 or higher.
  - Minimize prediction errors using MSE.

---

## Dashboard Design

The dashboard will consist of the following pages:

1. **Project Summary**:
   - Brief overview of the objectives, dataset, and key findings.

2. **Exploration Page**:
   - Interactive visualizations for analyzing correlations.
   - Heatmaps and scatter plots to showcase insights.

3. **Prediction Page**:
   - Input form for property details.
   - Real-time price predictions displayed dynamically.

4. **Model Evaluation Page**:
   - Performance metrics such as R² and MSE.
   - Feature importance visualization for interpretability.

---

## Unfixed Bugs

- No known unfixed bugs at this stage.
- Future iterations will address potential edge cases and user feedback from dashboard testing.

---

## Deployment

### Local Deployment

1. Clone the repository and install dependencies:
   ```bash
   git clone https://github.com/YOUR_REPO.git
   pip install -r requirements.txt
   ```

2. Run the Streamlit app locally:
   ```bash
   streamlit run app/app.py
   ```

### Heroku Deployment

1. Log into Heroku and create a new app:
   ```bash
   heroku login
   heroku create
   ```

2. Deploy the app to Heroku:
   ```bash
   git push heroku main
   ```

3. Ensure the `.python-version` file is set to a Heroku-supported Python version.

---

## Main Data Analysis and Machine Learning Libraries

- **Pandas**: Used for data manipulation and preprocessing.
- **Matplotlib/Seaborn**: Used for creating detailed visualizations.
- **Scikit-learn**: Used for machine learning model development and evaluation.
- **Streamlit**: Used for building the interactive web application.

---

## Credits

### Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data).

### Media

- Icons and dashboard assets are sourced from [Font Awesome](https://fontawesome.com/).
- The banner image is custom-designed using [Canva](https://www.canva.com/).

---

## Acknowledgements

- Special thanks to the Code Institute for providing guidance and resources for this project.
- Appreciation to mentors and peers for valuable feedback and support.

---

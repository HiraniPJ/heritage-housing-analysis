# Heritage Housing Analysis

## Table of Contents

1. [Introduction](#introduction)
2. [Business Requirements](#business-requirements)
3. [User Stories](#user-stories)
4. [Dataset Content](#dataset-content)
5. [Hypothesis and Validation](#hypothesis-and-validation)
6. [The Model](#the-model)
7. [Implementation of Business Requirements](#implementation-of-business-requirements)
8. [Dashboard Design](#dashboard-design)
9. [CRISP-DM Process](#crisp-dm-process)
10. [Requirements Evaluation](#requirements-evaluation)
11. [Improvements and Future Plans](#improvements-and-future-plans)
12. [Bugs](#bugs)
13. [Deployment](#deployment)
14. [Technologies Used](#technologies-used)
15. [Credits](#credits)
16. [Acknowledgements](#acknowledgements)

---

### Deployed version at [Heritage-Housing-Analysis](https://heritage-housing-analysis-347c30b4142b.herokuapp.com/)

---

## Introduction

The **Heritage Housing Analysis** project was initiated to support a client who inherited four houses in Ames, Iowa. The objective was to predict the potential sale prices of these properties using data analysis and machine learning. Additionally, the project provides tools and insights for visualizing how housing features impact property values.

The final product includes a deployed web application that allows users to upload property details and receive price predictions, explore data visualizations, and evaluate the predictive model.

---

## Business Requirements

The project fulfills the following key business requirements:

1. Visualize the relationship between house features and sale prices.
2. Predict the sale prices of the inherited houses and others in Ames.
3. Provide an interactive dashboard for users to explore insights and make predictions.
4. Offer actionable insights for property valuation and improvement.

---

## User Stories

### Must Have
1. As a client, I need accurate price predictions for my inherited houses to make informed decisions.
2. As a user, I need an interactive tool to explore housing data and trends.

### Should Have
1. As a client, I should receive clear visualizations to understand the relationship between housing features and sale prices.
2. As a user, I should receive guidance on improving property value.

### Could Have
1. As a client, I could receive trend analyses to anticipate future housing market conditions.
2. As a user, I could access detailed visualizations comparing inherited houses to Ames' market data.

---

## Dataset Content

The dataset is sourced from the **Ames Housing Dataset**, containing records of property features and sale prices. Key features include:

| Feature         | Description                              | Units    |
|------------------|------------------------------------------|----------|
| `GrLivArea`     | Above-grade living area                  | Sq. ft.  |
| `OverallQual`   | Overall material and finish quality      | 1-10     |
| `GarageArea`    | Garage size                              | Sq. ft.  |
| `YearBuilt`     | Year the house was built                 | Year     |
| `SalePrice`     | Sale price of the property               | USD      |

### Additional Datasets
1. **Inherited Houses Dataset**: Data for the four inherited properties.
2. **Training Data**: Historical housing data for training the predictive model.

---

## Hypothesis and Validation

### Hypothesis 1
- **Larger houses with better quality materials sell for higher prices.**
  - **Validation**: Correlation analysis between `GrLivArea`, `OverallQual`, and `SalePrice`.

### Hypothesis 2
- **Properties with recent renovations have higher sale prices.**
  - **Validation**: Regression analysis of `YearRemodAdd` versus `SalePrice`.

### Hypothesis 3
- **Garages and high-quality finishes significantly impact property values.**
  - **Validation**: Feature importance analysis from the regression model.

### Visuals
- Heatmaps, scatter plots, and box plots were used to validate these hypotheses.
- Add a placeholder for images: `![Heatmap Example](readme_images/heatmap.png)`

---

## The Model

The machine learning model used for this project is a **linear regression model** with the following details:

1. **Features Used**:
   - `GrLivArea`, `OverallQual`, `GarageArea`, `YearBuilt`.
2. **Training and Testing Split**:
   - 80% training, 20% testing.
3. **Performance Metrics**:
   - R² Score: **0.87**
   - Mean Squared Error (MSE): Low

### Code Snippet: Model Training
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```
---

## Implementation of Business Requirements

1. **Visualizations**:
   - Created scatter plots and heatmaps to show the relationship between housing features like `GrLivArea`, `OverallQual`, and `SalePrice`.
   - Demonstrated key trends in the dataset using box plots and distribution charts.

2. **Prediction**:
   - Developed a regression model for predicting house prices with high accuracy.
   - Ensured the predictions met the client's expectations for actionable insights.

3. **Dashboard**:
   - Built an interactive web application using Streamlit to allow users to explore data and generate predictions.

4. **Insights**:
   - Provided actionable insights into improving property values based on feature importance and prediction results.

### Example Insights Visualization
`![Insights Visualization](readme_images/insights_visualization.png)`

---

## Dashboard Design

The dashboard is designed to be intuitive and user-friendly, with the following sections:

1. **Project Summary**:
   - Overview of the objectives, key findings, and project details.
![image](https://github.com/user-attachments/assets/1d2136c7-001d-43f5-9d06-aa909dbe5da3)


2. **Data Exploration**:
   - Interactive visualizations to explore the dataset.
  ![image](https://github.com/user-attachments/assets/dae24a6f-50ae-48bb-b412-1e61377ecfa8)

   - Heatmaps and feature distribution charts.
![image](https://github.com/user-attachments/assets/5230b485-53ae-4cda-9e21-74d2e33ce687)

    - Scatter Plots
![image](https://github.com/user-attachments/assets/c92a20a9-9655-420e-a4dc-f39a1ad3cdeb)
![image](https://github.com/user-attachments/assets/1d027451-c5c5-4e1b-b9ef-7e6827c2231e)
![image](https://github.com/user-attachments/assets/98e601d7-8db2-4c9b-8d5f-9cb112d82497)

   - Box Plots for Key Features
![image](https://github.com/user-attachments/assets/e44581e7-08fd-4bad-a53c-0de9ca90508e)
![image](https://github.com/user-attachments/assets/d6480b0e-6968-4bda-9fef-a28e82a56507)
![image](https://github.com/user-attachments/assets/16b09e26-7cee-43a4-bb03-0ed6bbba56db)

   - Distribution Plots for Numeric Features
![image](https://github.com/user-attachments/assets/f977a1d7-40d7-4c17-a064-1df73b4b303b)
![image](https://github.com/user-attachments/assets/0f643853-247c-4c6e-aae3-22fe3264289e)
![image](https://github.com/user-attachments/assets/9f298030-8986-4e4d-a500-7ae5b252e7c8)
![image](https://github.com/user-attachments/assets/d4f5c44b-249f-4888-8fb8-d54fa135909c)


3. **Prediction Page and Model Evaluation**:
   - Input form for users to enter house attributes and receive price predictions in real-time.
   - Display confidence levels for each prediction.
   - 
![image](https://github.com/user-attachments/assets/c97deca3-235a-458e-9a91-7ea0f1299271)
![image](https://github.com/user-attachments/assets/8e414b1c-0988-495a-aebb-5767f3739f7e)


4. **Hypotheses and Validation**:

![image](https://github.com/user-attachments/assets/f4fdd759-2d4c-4720-9531-8b0580286cf6)


5. **Feedback and Reporting**
![image](https://github.com/user-attachments/assets/2c538eea-1d3f-4170-a59b-d1be657f04df)

---

## CRISP-DM Process

The CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology guided this project, ensuring a structured and efficient approach.

1. **Business Understanding**:
   - Defined key questions and objectives for predicting house prices and providing actionable insights.

2. **Data Understanding**:
   - Explored the dataset to identify trends, missing values, and correlations.

3. **Data Preparation**:
   - Cleaned the data, handled missing values, and prepared it for machine learning modeling.

4. **Modeling**:
   - Built and tuned a regression model to predict house prices.
   - Evaluated the model using metrics like R² score and MSE.

5. **Evaluation**:
   - Assessed the model's effectiveness in meeting business requirements.

6. **Deployment**:
   - Deployed the model and data visualizations into a Streamlit web application.

---

## Requirements Evaluation

### Business Requirement 1:
- **Visualize the relationship between house features and sale prices.**
  - **Outcome**: Achieved using scatter plots and heatmaps. Example below:
    `![Scatter Plot](readme_images/scatter_plot.png)`

### Business Requirement 2:
- **Predict the sale prices of inherited houses.**
  - **Outcome**: Delivered accurate price predictions with an R² score of 0.87.

### Business Requirement 3:
- **Provide an interactive dashboard.**
  - **Outcome**: Built a Streamlit app for real-time predictions and data exploration.

---

## Improvements and Future Plans

1. **Model Performance**:
   - Explore advanced regression techniques for better accuracy.
   - Integrate additional features to improve model interpretability.

2. **UI/UX Enhancements**:
   - Improve dashboard navigation and visual appeal.

3. **Feature Expansion**:
   - Add trend analysis for future property market forecasting.
   - Provide renovation recommendations based on model insights.

4. **Long-Term Goals**:
   - Incorporate machine learning techniques for advanced property valuation scenarios.

---

## Bugs

### Fixed Bugs
1. **Data Mismatch**:
   - Resolved incorrect merging of datasets, ensuring data consistency.

2. **Heroku Deployment**:
   - Fixed slug size issues by optimizing dependencies.

### Unresolved Bugs
- **None reported at this stage.**

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

## Technologies Used

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

---

## Acknowledgements

- Special thanks to the Code Institute for providing guidance and resources for this project.
- Appreciation to mentors and peers for valuable feedback and support.

---


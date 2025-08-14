# Heritage Housing Analysis

## Table of Contents

1. [Introduction](#introduction)
2. [Business Requirements](#business-requirements)
3. [Project Objectives](#project-objectives-and-success-criteria)
4. [User Stories](#user-stories)
5. [Dataset Content](#dataset-content)
6. [Hypothesis and Validation](#hypothesis-and-validation)
7. [The Model](#the-model)
8. [Implementation of Business Requirements](#implementation-of-business-requirements)
9. [Design and Testing](#design-and-testing)
10. [CRISP-DM Process](#crisp-dm-process)
11. [Requirements Evaluation](#requirements-evaluation)
12. [Improvements and Future Plans](#improvements-and-future-plans)
13. [Bugs](#bugs)
14. [Deployment](#deployment)
15. [Technologies Used](#technologies-used)
16. [Credits](#credits)
17. [Acknowledgements](#acknowledgements)

---

### Deployed version at [Heritage-Housing-Analysis](https://heritage-housing-analysis-347c30b4142b.herokuapp.com/)

---

## Introduction

My client is the executor of a small estate and has inherited four houses in Ames, Iowa. They must decide whether to **sell now, renovate and sell, or hold and rent**. They asked me to build a solution that provides:
-	A **defensible price estimate** for each property based on market-like data from Ames,
-	**Clear visibility into which features drive value** (so renovation money is spent where it matters),
-	An **interactive dashboard** to test “what-if” scenarios (e.g., “What if living area improves?”),
-	Evidence that the model **generalizes** to new properties (not just the training data).

I implemented:
-	A **Streamlit web app** that lets me enter house features and instantly get a predicted sale price.
-	A set of **exploratory visualizations** that show how house features relate to price in Ames.
-	A **machine-learning model** (Linear Regression) trained on the Ames dataset with evaluation metrics and cross-validation to demonstrate robustness.

---

## Business Requirements

The project fulfills the following key client's business requirements:

1. **Data Exploration & Visualization**
   
   Identify and clearly show the relationships between key features (e.g., GrLivArea, OverallQual, TotalBsmtSF, GarageArea) and sale price through static and interactive charts.

2. **Price Prediction**
   
   Deliver a machine-learning model capable of producing reliable price estimates for new properties, with target performance of Test R² ≥ 0.75 and transparent error metrics (MAE, RMSE).
   
3. **Interactive Dashboard**
   
   Provide a streamlined web app for real-time “what-if” estimation and data exploration, aligned to the model’s feature set.

4. **Actionable Insights**
   
   Translate findings into practical recommendations for pricing and renovation priorities.


## Project Objectives and Success Criteria

-	**O1. Build trustable predictions (Req 2).**
  
    _Success if:_ Test R² ≥ 0.75 and cross-validation R² is close to test R² (low variance).
  
    _Result:_
 	
-	**O2. Explain value drivers (Req 1 & 4).**
  
    _Success if:_ Visualizations and coefficients consistently show positive relationships for size/quality and the app exposes these relationships.
  
    _Result:_ 

-	**O3. Enable scenario testing (Req 3).**
  
    _Success if:_ The app accepts user inputs for the model’s features and returns a prediction instantly, with validation to avoid input mismatch.
  
    _Result:_

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
  - **Validation**: Confirmed using correlation heatmaps and scatter plots between `GrLivArea`, `OverallQual`, and `SalePrice`.

### Hypothesis 2
- **Properties with recent renovations have higher sale prices.**
  - **Validation**: Regression analysis of `YearRemodAdd` versus `SalePrice`.

### Hypothesis 3
- **Garages and high-quality finishes significantly impact property values.**
  - **Validation**: Feature importance analysis from the regression model.

### Visuals
- **Correlation Heatmaps** to understand feature relationships.
- **Box Plots** and **Scatter Plots** for feature-price impact assessment.
- **Distribution Plots** for analyzing price variations.


---

## The Model

## Machine Learning Model

The project implements a Linear Regression Model for predicting house prices. The model was chosen for its interpretability and performance on structured housing data.

### Key Model Details:

1. **Features Used**:
   - `GrLivArea`, `OverallQual`, `GarageArea`, `TotalBsmtSF`.
2. **Training and Testing Split**:
   - 80% training, 20% testing.
3. **Performance Metrics**:
   - **Train R² Score:** 0.745
   - **Test R² Score:** 0.791
   - **Mean Absolute Error (MAE):** $25,055.30
   - **Root Mean Squared Error (RMSE):** $40,046.56
   - **Cross-Validation R² Mean:** 0.735

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
   - Generated heatmaps, scatter plots, and box plots to illustrate key feature relationships.
   - Created interactive Plotly charts to enhance user exploration of data.
     
2. **Prediction Functionality**:
   - Developed a streamlit-based interactive prediction page where users can input house details and receive estimated sale prices.
   - Ensured the model performed well within acceptable error margins.

3. **Interactive Dashboard**:
   - Built a user-friendly Streamlit application that allows:
     - Price predictions based on house attributes.
     - Visual data exploration with both static and interactive charts.
     - Evaluation of the machine learning model’s accuracy and performance.

4. **Enhanced Insights**:
   - Provided clear insights into how different factors contribute to house pricing.
   - Suggested potential improvements and renovations to maximize property value.

---

## Design and Testing

The dashboard is designed to be intuitive and user-friendly, with the following sections:

1. **Project Summary**:
   - Overview of the objectives, key findings, and project details.
    ![image](https://github.com/user-attachments/assets/013845e0-8b3f-4ae7-a888-cb13e168d252)


2. **Data Exploration**:
   - **Interactive visualizations** to explore the dataset.
     
    ![image](https://github.com/user-attachments/assets/6174a873-b939-4d06-95b8-4ca5d9a4a2ba)


   - **Heatmaps** and feature distribution charts.
     
    ![image](https://github.com/user-attachments/assets/06509d54-e579-490c-897a-c90b431a85fe)


  - **Scatter Plots**
    
    ![image](https://github.com/user-attachments/assets/c92a20a9-9655-420e-a4dc-f39a1ad3cdeb)
    ![image](https://github.com/user-attachments/assets/1d027451-c5c5-4e1b-b9ef-7e6827c2231e)
    ![image](https://github.com/user-attachments/assets/98e601d7-8db2-4c9b-8d5f-9cb112d82497)


  - **Box Plots for Key Features**
    
    ![image](https://github.com/user-attachments/assets/e44581e7-08fd-4bad-a53c-0de9ca90508e)
    ![image](https://github.com/user-attachments/assets/d6480b0e-6968-4bda-9fef-a28e82a56507)
    ![image](https://github.com/user-attachments/assets/16b09e26-7cee-43a4-bb03-0ed6bbba56db)

   - **Sale Price Distribution (Interactive)**
    ![image](https://github.com/user-attachments/assets/0238da5f-d1ff-4d02-acf4-4b01de661f10)

   - **Living Area vs Sale Price (Interactive)**
    ![image](https://github.com/user-attachments/assets/84741835-9621-47b0-b636-444d3622c5e1)

   - **Garage Area vs Sale Price (Interactive)**
    ![image](https://github.com/user-attachments/assets/4ed4cbb9-1aa5-42bc-b227-16a6c7384fb1)


4. **Model Evaluation**:
   
    ![image](https://github.com/user-attachments/assets/c20310db-7520-466e-a9a3-743515fb64fe)

5. **Prediction Page Tested**

    ![image](https://github.com/user-attachments/assets/518e89fb-73b5-478d-b7fa-2d236d7203c1)

  - **Residual & Cross-Validation Score**
    
    ![image](https://github.com/user-attachments/assets/edf314ef-364a-4a09-93ad-d9f604ea2069)
    
    ![image](https://github.com/user-attachments/assets/b6d316cc-70f7-41c0-91d2-23c998897009)
    ![image](https://github.com/user-attachments/assets/094ffc28-6697-4cc9-ac31-488bc07081a0)
    

6. **Hypotheses and Validation**:

    ![image](https://github.com/user-attachments/assets/f4fdd759-2d4c-4720-9531-8b0580286cf6)


7. **Feedback and Reporting**
   
    ![image](https://github.com/user-attachments/assets/be286864-4c7f-441d-8e51-770c813f6899)

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
  - **Outcome**: Achieved using scatter plots and heatmaps. 

### Business Requirement 2:
- **Predict the sale prices of inherited houses.**
  - **Outcome**: Delivered accurate price predictions with an R² score of 0.87.

### Business Requirement 3:
- **Provide an interactive dashboard.**
  - **Outcome**: Built a Streamlit app for real-time predictions and data exploration.

---

## Improvements and Future Plans

1. **Enhancing Model Accuracy:**:
   - Fine-tune hyperparameters to improve performance.
   - Experiment with advanced machine learning models such as Random Forests and Gradient Boosting.

2. **Additional Features for User Interaction**:
   - Integrate automated recommendations for improving property value.
   - Allow users to compare multiple house predictions side by side.

3. **Expanding Data Sources:**:
   - Incorporate external housing market trends to refine predictions.

4. **Deployment & Optimization:**:
   - Optimize model loading for faster real-time predictions.
   - Deploy on cloud-based platforms for scalability.

---

## Bugs

### Fixed Bugs
1. **Data Mismatch**:
   - Resolved incorrect merging of datasets, ensuring data consistency.

2. **Heroku Deployment**:
   - Fixed slug size issues by optimizing dependencies.

### Resolved Bugs
- **Modeling and Evaluation Page Error.**
![image](https://github.com/user-attachments/assets/c089d47b-b213-42d6-a41e-bc650fa0b19d)

**Error Handling**
- Fixed KeyError: Replaced "R² Score" with "Test R²" as the correct metric key from model_metrics.json.
- Added Robust Key Checking: Prevents app crashes by verifying metric availability before accessing values.
- Displayed Cross-Validation Metrics: Now includes "Cross-Validation Mean R²" and "Cross-Validation Std Dev" for better model evaluation.
- Improved Interpretation Logic: Uses "Test R²" to classify model performance (Strong/Moderate/Poor).

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

- **Python**: Core programming language for data analysis and model building.
- **Pandas & NumPy**: Data manipulation and numerical computations.
- **Matplotlib/Seaborn**: Used for creating static data visualizations.
- **Scikit-learn**: Used for machine learning model development and evaluation.
- **Streamlit**: Used for building the interactive web application.
- **Plotly**: Interactive data visualization.
- **Joblib**: Model persistence and storage.

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


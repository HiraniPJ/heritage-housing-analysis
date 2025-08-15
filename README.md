# Heritage Housing Analysis

## Table of Contents

1. [Introduction](#introduction)
2. [Business Requirements](#business-requirements)
3. [Project Objectives](#project-objectives-and-success-criteria)
4. [User Stories](#user-stories)
5. [Dataset Content](#dataset-content)
7. [The Model](#the-model)
8. [Hypothesis and Validation](#hypothesis-and-validation)
9. [Implementation of Business Requirements](#implementation-of-business-requirements)
10. [Design and Testing](#design-and-testing)
11. [CRISP-DM Process](#crisp-dm-process)
12. [Requirements Evaluation](#requirements-evaluation)
13. [Improvements and Future Plans](#improvements-and-future-plans)
14. [Bugs](#bugs)
15. [Deployment](#deployment)
17. [Technologies Used](#technologies-used)
18. [Credits](#credits)
19. [Acknowledgements](#acknowledgements)

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
  
    **_Result:_** Test R² = 0.791, CV mean R² = 0.735, CV std = 0.072 → **Met.**
 	
-	**O2. Explain value drivers (Req 1 & 4).**
  
    _Success if:_ Visualizations and coefficients consistently show positive relationships for size/quality and the app exposes these relationships.
  
    **_Result:_** GrLivArea and OverallQual strongly positive; TotalBsmtSF and GarageArea positive with smaller effects → **Met.**

-	**O3. Enable scenario testing (Req 3).**
  
    _Success if:_ The app accepts user inputs for the model’s features and returns a prediction instantly, with validation to avoid input mismatch.
  
    **_Result:_** Streamlit Prediction page implemented and validated → **Met.**

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

**Split used for modelling: 80% train / 20% test** (random_state=42). 

### Additional Datasets
1. **Inherited Houses Dataset**: Data for the four inherited properties.
2. **Training Data**: Historical housing data for training the predictive model.

---

## The Model

## Machine Learning Model

The project implements a Linear Regression Model for predicting house prices. The model was chosen for its interpretability and performance on structured housing data.

### Key Model Details:

1. **Features Used**:
   - `GrLivArea`, `OverallQual`, `GarageArea`, `TotalBsmtSF`.
2. **Training and Testing Split**:
   - **Split strategy:** 80% train / 20% test  
   - **Cross-validation:** 5-fold K-Fold on the full feature set  
   - **Why this matters:** The **Test R²** reflects out-of-sample generalization, and the **CV R² (mean ± std)** demonstrates robustness across folds.
3. **Performance Metrics**:
   - **Train R² Score:** 0.745
   - **Test R² Score:** 0.791
   - **Mean Absolute Error (MAE):** $25,055.30
   - **Root Mean Squared Error (RMSE):** $40,046.56
   - **Cross-Validation R² Mean:** 0.735 (5-fold), **Std Dev:** 0.072

### Code Snippet: Model Training
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```
---

## Hypothesis and Validation

### Hypothesis 1 - Size & Quality Premium
-  _Hypothesis:_ Larger living area and higher material quality are associated with higher SalePrice.**
- **Evidence:**  
  - Positive slopes in **GrLivArea vs SalePrice** and **OverallQual vs SalePrice** charts (interactive).  
  - Correlation heatmap shows strong positive association between these features and SalePrice.
-  _Outcome:_ **Supported** (Objective O2 met).
-  _**Box Plots**_
     <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/877eda96-167b-4a41-a4a0-ba6d386a89d5" />
     
     <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/13005e95-835c-4660-be8d-cb463760471c" />

     <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/dd97f46c-780c-43a9-bd50-13c235bd9a7e" />
 

### Hypothesis 2 - Renovation Effect
-  _Hypothesis:_ Properties with recent renovations have higher sale prices.
- **Evidence:**  
  - **GarageArea vs SalePrice** and **TotalBsmtSF vs SalePrice** show positive trends.  
  - Model coefficients rank these as positively weighted features.
-  _Outcome:_ **Supported** secondary to GrLivArea/OverallQual.
-  _**GarageArea vs SalePrice**_

       <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/75c73b7e-6731-463b-b9b6-e3cd56b396a5" />
        
- **_TotalBsmtSF Distribution_**
  
       <img width="897" height="580" alt="image" src="https://github.com/user-attachments/assets/7c4034b6-00cd-4eb4-899f-eee1c6077384" />


### Hypothesis 3 - The predictive model generalizes well to unseen data.
-  _Hypothesis:_ Garages and high-quality finishes significantly impact property values.
- **Evidence (from `outputs/model_metrics.json`):**  
  - **Train R²:** 0.745  
  - **Test R²:** 0.791  
  - **MAE:** $25,055.30  
  - **RMSE:** $40,046.56  
  - **5-fold CV R²:** 0.735 ± 0.072   
  - **Plots:** Actual vs Predicted (test), Residuals vs Predicted, CV distribution.  
-  _Outcome:_ **Supported** (The model shows solid generalization and stable CV performance).
-  _**Actual vs Predicted Sale Price**_
     
    <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/13e0ac84-7c49-44c3-bac7-f44366569048" />

   - **Residual & Cross-Validation Score**
     
     <img width="500" height="700" alt="image" src="https://github.com/user-attachments/assets/727271f9-d917-41d3-a89d-3bb27cb260c3" />

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

### Visuals
- **Correlation Heatmaps** to understand feature relationships.
- **Box Plots** and **Scatter Plots** for feature-price impact assessment.
- **Distribution Plots** for analyzing price variations.

1. **Project Summary**:
   - Overview of the objectives, key findings, and project details.
     
   <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/2afc083f-f953-417e-9ac4-cdf9bf217294" />


2. **Data Exploration**:
   
   - **Interactive visualizations** to explore the dataset.
     
    <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/6174a873-b939-4d06-95b8-4ca5d9a4a2ba" />


   - **Sale Price Distribution (Interactive)**
  
      <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/1d364489-4c18-4406-9705-b86f4a6a3a01" />

   - **Living Area vs Sale Price (Interactive)**
     
      <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/4ea81514-d5f3-48a8-8c97-0f00c463b372" />

   - **Garage Area vs Sale Price (Interactive)**
     
      <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/c879e7a8-c2f0-4b96-b277-0ae4b22471a3" />


4. **Model Evaluation**:
   
   <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/85f546d4-ad38-45a6-9c63-11a67998ee8a" />
   

5. **Prediction Page Tested**

    <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/28c9bec7-0388-4675-8322-3828ff0b9cc2" />
    

6. **Hypotheses and Validation**:

    <img width="500" height="700" alt="image" src="https://github.com/user-attachments/assets/9b8387d5-f4d7-4767-8dc2-5e1c7154f82a" />


7. **Feedback and Reporting**
   
    <img width="400" height="700" alt="image" src="https://github.com/user-attachments/assets/be286864-4c7f-441d-8e51-770c813f6899" />

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

### Business Requirement 1: **Data Exploration & Visualization**
- Visualize the relationship between house features and sale prices.
  - **Success criteria:** At least three feature–price visualizations with a short interpretation explaining what each means for pricing decisions. 

### Business Requirement 2: **Price Prediction**
- Predict the sale prices of inherited houses.
  - **Outcome**: Delivered accurate price predictions with **Train R²**, **Test R²**, **MAE**, **RMSE**, and **5-fold CV R² (mean ± std)** on the app’s “Modeling & Evaluation” page.

### Business Requirement 3: **Interactive Dashboard** 
- Provide an interactive dashboard.
  - **Success criteria:** Prediction page loads the trained model successfully and returns a price with validation of feature inputs.

### Business Requirement 4: **Actionable Insights**
- Offer strategic recommendations backed by data (e.g., “improving OverallQual has a stronger marginal impact than increasing GarageArea”).
  - **Success criteria:** A short, evidence-based conclusions section that cites the model coefficients/plots and the evaluation metrics.

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
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/c089d47b-b213-42d6-a41e-bc650fa0b19d" />

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


## Prediction Page (How-To)

1. Go to **Prediction** in the left sidebar.  
2. Enter values for: `GrLivArea`, `OverallQual`, `GarageArea`, `TotalBsmtSF`.  
3. Click **Predict House Price**.  
4. The app validates your inputs and displays an estimated price.

**Troubleshooting**  
- If you see: `AttributeError: 'tuple' object has no attribute 'predict'`  
  This indicates the serialized object isn’t a fitted model. Re-train and save via the notebook:  
  - Ensure you save **only** the fitted model object (not a tuple) to `outputs/trained_model.pkl`.  
  - Confirm the prediction page loads it with `joblib.load('outputs/trained_model.pkl')` and calls `.predict(...)` on a DataFrame with the **same feature order** used in training.
   
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


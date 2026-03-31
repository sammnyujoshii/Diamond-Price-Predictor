# AI Diamond Price Predictor (Web App)

** Live Web App:** [https://diamond-price-predictor-bfpsjhtiqwb9wuvv3dr2cf.streamlit.app/]

## Overview
This Machine Learning project predicts the market price of diamonds based on their physical attributes (Carat, Cut, Color, and Clarity). It features a trained AI model and an interactive web frontend where users can input diamond specifications to get real-time price estimations in Indian Rupees (INR).

## Architecture & Methodology
The project treats diamond pricing as a Supervised Regression problem, utilizing a **Random Forest Regressor** to identify non-linear pricing patterns. The application is divided into two distinct parts for professional performance:

1. **The Brain (`train_model.py`):** Trains the Random Forest on a publicly available dataset of ~54,000 diamonds and saves the model's state using `joblib`.
2. **The Face (`app.py`):** An interactive web interface built with **Streamlit** that loads the saved model and processes live user inputs without needing to retrain the data.

## Implementation Details
* **Data Preprocessing:** Categorical text features (like Cut and Color) were converted into numerical arrays using One-Hot Encoding (`pd.get_dummies`) so the machine learning algorithm could process them.
* **Model Training:** The `RandomForestRegressor` was trained using 50 estimators (decision trees) to ensure high accuracy and prevent overfitting.
* **Currency Conversion:** Output predictions are dynamically converted from USD to INR for local market relevance.

## Project Structure
* `train_model.py` - The backend script that fetches data, trains the model, and saves it.
* `app.py` - The Streamlit frontend web application.
* `diamond_model.pkl` - The saved memory/weights of the trained Random Forest model.
* `model_columns.pkl` - The saved data structure required for user inputs.
* `requirements.txt` - The library dependencies required for cloud deployment.

## How to Run Locally
1. Install dependencies: 
   `pip install pandas scikit-learn streamlit joblib`
2. Train the model (only needed once): 
   `python train_model.py`
3. Launch the web app: 
   `streamlit run app.py`
   `streamlit run app.py`

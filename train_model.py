import ssl
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib


ssl._create_default_https_context = ssl._create_unverified_context

print("1. Downloading dataset...")
url = "https://raw.githubusercontent.com/tidyverse/ggplot2/master/data-raw/diamonds.csv"
diamonds_data = pd.read_csv(url)


data = diamonds_data[['carat', 'cut', 'color', 'clarity', 'price']].copy()

print("2. Formatting the data...")

data = pd.get_dummies(data, columns=['cut', 'color', 'clarity'])

X = data.drop('price', axis=1) 
y = data['price']              

print("3. Training the AI (this takes about 15 seconds)...")
model = RandomForestRegressor(n_estimators=50, random_state=42)

model.fit(X, y) 

print("4. Saving the trained model...")

joblib.dump(model, 'diamond_model.pkl')
joblib.dump(X.columns.tolist(), 'model_columns.pkl')

print("SUCCESS! The model is saved and ready for the Streamlit app.")
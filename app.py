import streamlit as st
import pandas as pd
import joblib


model = joblib.load('diamond_model.pkl')
model_columns = joblib.load('model_columns.pkl')


st.set_page_config(page_title="Diamond Pricer", page_icon="")
st.title(" AI Diamond Price Predictor")
st.write("Enter the physical attributes of your diamond below to get an estimated market value.")

st.markdown("---")


col1, col2 = st.columns(2)

with col1:
   
    carat = st.number_input("Weight in Carats (1 Carat = 0.2 grams)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
    
 
    cut = st.selectbox("Cut Quality (Sharpness/Proportion)", ["Fair", "Good", "Very Good", "Premium", "Ideal"])

with col2:
    
    color = st.selectbox("Color Grade (D is perfectly clear, J has a yellow tint)", ["D", "E", "F", "G", "H", "I", "J"])
    clarity = st.selectbox("Clarity (Internal flaws. IF is flawless, I1 is heavily flawed)", ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])

st.markdown("---")


if st.button("Calculate Estimated Price"):
    
    # Create an empty dataframe with all zeros
    input_data = pd.DataFrame(columns=model_columns)
    input_data.loc[0] = 0 
    
    # Fill in the user's carat weight
    input_data['carat'] = carat
    
  
    if f'cut_{cut}' in model_columns:
        input_data[f'cut_{cut}'] = 1
    if f'color_{color}' in model_columns:
        input_data[f'color_{color}'] = 1
    if f'clarity_{clarity}' in model_columns:
        input_data[f'clarity_{clarity}'] = 1

  
    usd_price = model.predict(input_data)[0]
    
   
    inr_price = int(usd_price * 83)
    
   
    st.success(f"### Estimated Value: ₹ {inr_price:,}")
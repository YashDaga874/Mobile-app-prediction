import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load pre-trained model and data
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title('Mobile Price Predictor')

# Define Streamlit widgets for user input
company = st.selectbox('Brand', df['brand_name'].unique())
Number_of_sims = st.selectbox('Number of sims', [1, 2])
has_5g = st.selectbox('Supports 5G? (0 for No, 1 for Yes)', [0, 1])
has_nfc = st.selectbox('Supports NFC? (0 for No, 1 for Yes)', [0, 1])
has_ir_blaster = st.selectbox('Supports IR Blaster? (0 for No, 1 for Yes)', [0, 1])
processor_name = st.selectbox('Processor Brand', df['processor_name'].unique())
num_cores = st.selectbox('Number of Cores', df['num_cores'].unique())
processor_speed = st.selectbox('Processor Speed', df['processor_speed'].unique())
ram = st.selectbox('RAM Capacity', df['ram'].unique())
battery_capacity = st.selectbox('Battery Capacity', df['battery_capacity'].unique())
fast_charging = st.selectbox('Fast Charging Support', df['fast_charging'].unique())
internal_memory = st.selectbox('Internal Memory', df['internal_memory'].unique())
screen_size = st.slider('Screen Size (inches)', min_value=3.0, max_value=10.0, step=0.1)
refresh_rate = st.selectbox('Refresh Rate', df['refresh_rate'].unique())
num_rear_cameras = st.selectbox('Number of Rear Cameras', df['num_rear_cameras'].unique())
num_front_cameras = st.selectbox('Number of Front Cameras', df['num_front_cameras'].unique())
card = st.selectbox('Card Type', df['card'].unique())
os = st.selectbox('Operating System', df['os'].unique())
primary_camera_rear = st.selectbox('Primary Rear Camera Resolution', df['primary_camera_rear'].unique())
primary_camera_front = st.selectbox('Primary Front Camera Resolution', df['primary_camera_front'].unique())
extended_memory = st.selectbox('Extended Memory Support', df['extended_memory'].unique())
res_width = st.selectbox('Resolution Width', df['res_width'].unique())
res_height = st.selectbox('Resolution Height', df['res_height'].unique())
is_foldable = st.selectbox('Is Foldable? (0 for No, 1 for Yes)', [0, 1])

processor_brand = df['processor_name'].str.split(' ').str.get(0).str.lower()

ppi = int(((res_width ** 2 + res_height ** 2) ** 0.5) / screen_size)
aspect_ratio = res_width / res_height
screen_area = (res_width * res_height) / (ppi **2)

# Predict price based on user input
if st.button('Predict Price'):
    query = np.array([[company, has_5g, has_nfc, has_ir_blaster, processor_name, processor_brand, num_cores, processor_speed,ram, battery_capacity, fast_charging, internal_memory, screen_size, refresh_rate,num_rear_cameras, num_front_cameras, card, os, primary_camera_rear, primary_camera_front,extended_memory, res_width, res_height, ppi, aspect_ratio, screen_area, is_foldable,Number_of_sims]])
    
    query = query.reshape(1, -1)
  # Reshape query into a single sample
    st.title(pipe.predict(query))
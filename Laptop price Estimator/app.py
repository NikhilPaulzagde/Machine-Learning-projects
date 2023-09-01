import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the pre-trained model
pipe = pickle.load(open('pipe.pkl','rb'))

# Load the DataFrame
df = pd.read_pickle(open('df.pkl','rb'))

st.set_page_config(
    page_title="Laptop Predictor",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS styles
st.markdown(
    """
    <style>
    body {
        background-color: #f5f7f9;
    }
    
    .sidebar .sidebar-content {
        background-color: #f5f7f9;
    }
    
    .predict-button {
        background-color: #ff6f00;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        animation: pulse 1s infinite;
        transition: opacity 0.3s ease-in-out;
    }
    
    .predict-button:hover {
        opacity: 0.8;
    }
    
    @keyframes pulse {
        0% {
            transform: scale(1);
            box-shadow: 0 0 0 0 rgba(255, 111, 0, 0.7);
        }
        50% {
            transform: scale(1.05);
            box-shadow: 0 0 0 15px rgba(255, 111, 0, 0);
        }
        100% {
            transform: scale(1);
            box-shadow: 0 0 0 0 rgba(255, 111, 0, 0.7);
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)




# Custom color palette
custom_palette = ["#256eff", "#ff3d00", "#00c853", "#6200ea", "#d50000"]
sns.set_palette(custom_palette)

# Page header
header_html = """
    <div style="background-color:#256eff;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">Laptop Predictor</h1>
    <p style="color:white;text-align:center;">Predict the price of a laptop based on its specifications</p>
    </div>
"""
st.markdown(header_html, unsafe_allow_html=True)

# brand
company = st.selectbox('Brand',df['Company'].unique())

# type of laptop
type = st.selectbox('Type',df['TypeName'].unique())

# Ram
ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

# weight
weight = st.number_input('Weight of the Laptop')

# Touchscreen
touchscreen = st.selectbox('Touchscreen',['No','Yes'])

# IPS
ips = st.selectbox('IPS',['No','Yes'])

# screen size
screen_size = st.number_input('Screen Size')

# resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#cpu
cpu = st.selectbox('CPU',df['Cpu brand'].unique())

hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',df['Gpu_Brand'].unique())

os = st.selectbox('OS',df['Os'].unique())

if st.button('Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = (np.sqrt((X_res**2) + (Y_res**2)))/screen_size
    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

    query = query.reshape(1,12)
    st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))

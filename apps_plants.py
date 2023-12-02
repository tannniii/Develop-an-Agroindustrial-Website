import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

#Load 
def load_data():
    data = pd.read_csv('sf.csv')
    return data

def descriptive_analysis(data):
    return data.describe()


def plot_distribution(data, column):
    plt.figure(figsize=(10,6))
    sns.histplot(data[column],kde=True)
    plt.title(f"Distribution {column}")
    plt.xlabel(column)
    plt.ylabel('Frequency')
    
    mean_val = data[column].mean()
    plt.axvline(mean_val, color='r', linestyle='dashed',linewidth=2)
    plt.text(mean_val*1.1, plt.ylim()[1]*0.9,f'Rata-rata:{mean_val:.2f}', color='r')
    st.pyplot(plt)       
    
data = load_data()
st.title("🌾 Analyze of Smart Farming Data")

#Menu
st.sidebar.title(' 🔍 Navigation')
page = st.sidebar.radio("Navigation Menu",
                        [':house: Title', ':memo: Data Explanation', ':bar_chart: Data Image',':chart_with_upwards_trend: Data Visualization'])



if page == ':house: Title':
    st.image('gambargif.gif',use_column_width=True)
    st.header('Welcome to Smart Farming Web Data Analysis:bar_chart:')
    st.write('This Website Give Analysis About Agricultural Condition.')
    st.write('The dataset contains information about the growth conditions of various crops, including measurements of Nitrogen (N), Phosphorus (P), and Potassium (K) levels in the soil, as well as environmental factors such as temperature, humidity, pH level, and rainfall. The "label" column indicates the type of crop being grown. This data can be used to analyze the optimal growing conditions for different crops, monitor farming practices, and make informed decisions to improve crop yield and quality. It provides valuable insights for farmers and agricultural researchers to optimize farming techniques and enhance agricultural productivity.')
    st.write('The motivational points of the data include: 1. Empowering farmers to optimize farming techniques and enhance agricultural productivity. 2. Providing valuable insights for making informed decisions to improve crop yield and quality.    3. Enabling the agricultural community to adapt and innovate in order to achieve sustainable and efficient farming practices.')
    st.write('The challenge of the data lies in leveraging the diverse set of factors and measurements to identify the optimal growth conditions for different crops. This involves analyzing the complex interplay between soil nutrients, environmental variables, and crop types to develop effective farming strategies. Additionally, ensuring the accuracy and reliability of the data is crucial for making informed decisions and recommendations. The challenge also includes the need to translate the data into actionable insights that can be practically applied by farmers to improve crop yield and quality.')
elif page ==':memo: Data Explanation':
    st.header('Data Explanation')
    st.write("""
    This data Contains information about Agricultural condition, including :
    - Nitrogen (N)
    - Phospor (P)
    - Pottasium (K)
    - Temperature
    - Humidity
    - Potential of Hydrogen (pH)
    - Rainfall
    - Crops Labell
    
    This is Raw Data Sample Used in website :
    """)
    st.dataframe(data) 

elif page ==':bar_chart: Data Image':
    st.header('Data Description')
    st.write('This is Descriptive Analysis from dataset:')
    st.dataframe(descriptive_analysis(data))
    

elif page ==':chart_with_upwards_trend: Data Visualization':
    st.header('Data Visualization')
    columns_to_visualize = data.columns.drop('label')
    # Pilihan kolom untuk visualisasi tanpa 'Row Labels'
    column = st.selectbox('Choose Clumn for Visualisation', columns_to_visualize)
    plot_distribution(data, column)
    
    st.write(f"""
    Graphic above shows distribution Column Value'{column}'. Red dashed line showed average value.
    it cann help to understand distribution data and to Identify common or unusual value.
    """)

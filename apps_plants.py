import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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
st.title("Analyze of Smart Farming Data")

#Menu
st.sidebar.title('Navigation')
page = st.sidebar.radio("Navigation Menu",
                        [':house: Title', ':memo: Data Explanation', ':bar_chart: Data Image',':chart_with_upwards_trend: Data Visualization'])


if page == ':house: Title':
    st.header('Welcome to Smart Farming Web Data Analysis:bar_chart:')
    st.write('This Website Give Analysis About Agricultural Condition.')

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
    column = st.selectbox('Pilih Kolom untuk Visualisasi', columns_to_visualize)
    plot_distribution(data, column)
    
    st.write(f"""
    Grafik di atas menunjukkan distribusi nilai kolum'{column}'. Garis putus-putus merah menunjukkan rata-rata nilai.
    Hal ini dapat membantu dalam memahami sebaran data dan mengidentifikasi nilai yang umum atau tidak biasa.
    """)
    
    
    
    st.write('Distribusi Label Tanaman:')
    plt.figure(figsize=(10,6))
    ax = sns.countplot(data=data, x='label')
    plt.xticks(rotation=45)
    plt.title('Ditribusi label tanaman')
    plt.xlabel('label Tanaman')
    plt.ylabel('Jumlah')
    
    st.pyplot(plt)
    

    
    
    




            
        






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
    plt.title(f"Distribusi {column}")
    plt.xlabel(column)
    plt.ylabel('Frekuensi')
    
    mean_val = data[column].mean()
    plt.axvline(mean_val, color='r', linestyle='dashed',linewidth=2)
    plt.text(mean_val*1.1, plt.ylim()[1]*0.9,f'Rata-rata:{mean_val:.2f}', color='r')
    st.pyplot(plt)       
    
data = load_data()
st.title("Analisi Data Pertanian")

#Menu
st.sidebar.title('Navigasi')
page = st.sidebar.radio("Menu Navigation",
                        [':house: Judul', ':memo: Penjelasan Data', ':bar_chart: Gambar Data',':chart_with_upwards_trend: Visualisasi Data'])


if page == ':house: Judul':
    st.header('Selamat Datang di Web Analisis Data Pertanian :bar_chart:')
    st.write('Aplikasi ini memberikan Analisis Tentang kondisi pertanian.')

elif page ==':memo: Penjelasan Data':
    st.header('Penjelasan Data')
    st.write("""
    Data ini berisi informasi mengenai kondisi pertanian yang meliputi :
    - Nitrogen (N)
    - Fosfor (P)
    - Kalium (K)
    - Suhu
    - Kelembapan
    - pH
    - Curah Hujan
    - Label Tanaman
    
    Berikut adalah Sample Data Mentah yang digunakan dalam web ini :
    """)
    st.dataframe(data) 

elif page ==':bar_chart: Gambar Data':
    st.header('Gambaran Data')
    st.write('Berikut adalah analisis deskriptif dari datasetL:')
    st.dataframe(descriptive_analysis(data))
    

elif page ==':chart_with_upwards_trend: Visualisasi Data':
    st.header('Visualisasi Data')
    column = st.selectbox('Pilih Kolom Untuk Visualisasi', data.columns)
    plot_distribution(data,column)
    
    st.write(f"""
    Grafik di atas menunjukkan distribusi nilai kolum '{column}'. Garis putus-putus merah menunjukkan rata-rata nilai.
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
    
    

    
    
    




            
        






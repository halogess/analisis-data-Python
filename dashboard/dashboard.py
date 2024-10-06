import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dashboard/hour.csv") 

# Dashboard title
st.title("Bike Sharing Dashboard")

# Sidebar filters
st.sidebar.header("Filter Data")

# Filter untuk memilih working day atau tidak
workingday_option = st.sidebar.selectbox(
    "Pilih Tipe Hari", 
    ("Workday", "Weekend")
)

# Filter data berdasarkan pilihan working day
if workingday_option == "Workday":
    data_filtered = df[df['workingday'] == 1]
    st.subheader("Data Sewa Sepeda pada Hari Kerja")
else:
    data_filtered = df[df['workingday'] == 0]
    st.subheader("Data Sewa Sepeda pada Akhir Pekan")

# Menampilkan tabel data
st.dataframe(data_filtered.head())

# Grafik rata-rata sewa sepeda per jam berdasarkan filter
average_rent_by_hour = data_filtered.groupby('hr')['cnt'].mean().reset_index()

# Plotting the graph
plt.figure(figsize=(10,6))
sns.barplot(x='hr', y='cnt', data=average_rent_by_hour, palette="Blues_d")
plt.title(f"Rata-rata Sewa Sepeda per Jam - {workingday_option}")
plt.xlabel("Jam")
plt.ylabel("Rata-rata Jumlah Sewa")
st.pyplot(plt)

# Grafik total sewa berdasarkan kondisi cuaca
total_rent_by_weather = df.groupby('weathersit')['cnt'].sum().reset_index()

# Mengganti nilai numerik dengan string deskriptif
weather_mapping = {
    1: 'Clear, Few clouds',
    2: 'Mist + Cloudy',
    3: 'Light Snow, Rain',
    4: 'Heavy Rain, Storm'
}
total_rent_by_weather['weathersit'] = total_rent_by_weather['weathersit'].replace(weather_mapping)

# Membuat barplot untuk total rental berdasarkan cuaca
plt.figure(figsize=(8,6))
sns.barplot(x='weathersit', y='cnt', data=total_rent_by_weather, palette="coolwarm")
plt.title("Total Sewa Sepeda Berdasarkan Cuaca")
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Total Jumlah Sewa")
plt.xticks(rotation=45)
st.pyplot(plt)

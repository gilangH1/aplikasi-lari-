import streamlit as st
import time
import folium
from streamlit_folium import st_folium
from geopy.distance import geodesic
from calori import calculate_calories

# Mengatur page title
st.set_page_config(page_title="Aplikasi Lari ", page_icon="🏃", layout="centered")


# Sidebar untuk aplikasi lari 
st.sidebar.title("🚶‍♂️Aplikasi Lari ")

# Pilihan menu
app_mode = st.sidebar.radio("Pilih Fitur", ["Pelacakan GPS", "Waktu Lari", "Pengukuran  Waktu", "Perhitungan Kalori"])

# Fungsi menu aplikasi lari
def app():
    if app_mode == "Pelacakan GPS":
        gps_tracking()
    elif app_mode == "Waktu Lari":
        time_tracking()
    elif app_mode == "Pengukuran  Waktu":
       convert_distance_to_time()
    elif app_mode == "Perhitungan Kalori":
        calorie_calculation()

#  fungsi GPS tracking
def gps_tracking():
    st.header(" Pelacakan GPS ")
    #fungsi Mencari lokasi 
    location = st.text_input("Masukkan lokasi  (misalnya: lat, long):", "0,0")
    
    if location:
        lat, lon = map(float, location.split(','))
        peta = folium.Map(location=[-5.0, 120.0], zoom_start=4)
        folium.Marker([lat, lon], popup="Lokasi Saat Ini").add_to(peta)
        st_folium(peta, width=700, height=500)

# Fungsi mengukuran waktu lari
def time_tracking():
    st.subheader("🕰️ Waktu")
    start_time = st.button("Mulai Lari")
    if start_time:
            st.session_state.start_time = time.time()
            st.write("🏃‍♂️Lari dimulai")
        
    if 'start_time' in st.session_state:
            elapsed_time = time.time() - st.session_state.start_time
            st.info(f"Total Waktu: {elapsed_time:.2f} detik")
            if st.button("Selesai Lari" ):
                st.session_state.end_time = time.time()      

# Fungsi pengukur waktu tujuan
def convert_distance_to_time():
    st.header("Konverter Jarak ke Waktu")
    distance = st.number_input("Masukkan jarak (km):",  min_value=0)
    speed = st.number_input("Masukkan kecepatan (km/jam):",  min_value=0)

    if speed == 0:
        st.write("Kecepatan .")
    else:
        time = distance / speed
        st.write(f"Waktu yang dibutuhkan: {time} jam")
    
# Fungsi menghitungan kalori
def calorie_calculation():
    st.header("Kalori")
    distance = st.number_input("Masukkan jarak tempuh (dalam km):",  min_value=0)
    weight = st.number_input("Masukkan berat badan (dalam kg):",  min_value=0)
    
    if distance and weight:
        calories_burned = calculate_calories(distance, weight)
        st.write(f"Kalori yang terbakar: {calories_burned} kalori")

if __name__ == "__main__":
    app()
    
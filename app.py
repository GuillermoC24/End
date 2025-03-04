import streamlit as st
import pandas as pd
from prediction import predict

# Título de la aplicación
st.title("Predicción de Precios de Viviendas")

# Entrada de datos desde la interfaz de usuario
longitude = st.number_input("Longitud", step=0.01)
latitude = st.number_input("Latitud", step=0.01)
housing_median_age = st.number_input("Edad mediana de la vivienda", step=1)
total_rooms = st.number_input("Total de habitaciones", step=1)
total_bedrooms = st.number_input("Total de dormitorios", step=1)
population = st.number_input("Población", step=1)
households = st.number_input("Hogares", step=1)
median_income = st.number_input("Ingreso medio", step=0.01)
ocean_proximity = st.selectbox("Proximidad al océano", ["<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"])

# Botón para realizar la predicción
if st.button("Predecir"):
    # Crear un DataFrame con los datos de entrada
    input_data = pd.DataFrame({
        "longitude": [longitude],
        "latitude": [latitude],
        "housing_median_age": [housing_median_age],
        "total_rooms": [total_rooms],
        "total_bedrooms": [total_bedrooms],
        "population": [population],
        "households": [households],
        "median_income": [median_income],
        "ocean_proximity": [ocean_proximity]
    })
    
    # Realizar la predicción
    try:
        prediction = predict(input_data)
        st.success(f"El precio predicho es: ${prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Error al realizar la predicción: {e}")
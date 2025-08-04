import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.title("Análisis de Autos")

# Crear un pequeño DataFrame de ejemplo
data = {
    "Marca": ["Toyota", "Ford", "BMW", "Nissan"],
    "Precio": [20000, 25000, 40000, 22000],
    "Año": [2020, 2019, 2021, 2018]
}
df = pd.DataFrame(data)

# Mostrar los datos
st.subheader("Datos de autos")
st.write(df)

# Crear un gráfico interactivo
fig = px.bar(df, x="Marca", y="Precio", color="Año", title="Precios por Marca")
st.plotly_chart(fig)

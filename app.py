import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Encabezado principal de la app
st.header('Análisis de vehículos en venta en EE. UU.')

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# -----------------------------------
# Casilla 1: Mostrar histograma
# -----------------------------------
show_hist = st.checkbox('Mostrar histograma del odómetro')

if show_hist:
    st.write('Histograma del odómetro (kilometraje) de los vehículos')

    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------------
# Casilla 2: Mostrar gráfico de dispersión
# -----------------------------------
show_scatter = st.checkbox('Mostrar gráfico de dispersión: precio vs. año del modelo')

if show_scatter:
    st.write('Gráfico de dispersión: Precio vs Año del Modelo')

    fig_scatter = go.Figure(
        data=go.Scatter(
            x=car_data['model_year'],
            y=car_data['price'],
            mode='markers',
            marker=dict(color='blue', opacity=0.5)
        )
    )

    fig_scatter.update_layout(
        title='Precio vs. Año del Modelo',
        xaxis_title='Año del Modelo',
        yaxis_title='Precio'
    )

    st.plotly_chart(fig_scatter, use_container_width=True)





import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")
st.header("Car Data")

# Foi adicionado um botão para mostrar o histograma
hist_button = st.button("Show Histogram")

#Aqui foi criado um histograma para o conjunto de dados de anuncios de venda de carros
if hist_button:
    st.write("Criando um histograma para o conjunto de dados de anuncios de venda de carros")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Foi adicionado um botão para mostrar o gráfico de dispersão
scatter_button = st.button("Show Scatter Plot")
# Aqui foi criado um gráfico de dispersão para o conjunto de dados de anuncios de venda de carros
if scatter_button:
    st.write("Criando um gráfico de dispersão para o conjunto de dados de anuncios de venda de carros")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)


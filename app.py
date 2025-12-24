import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Análisis de Vehículos", page_icon="🚗", layout="wide")

car_data = pd.read_csv('vehicles_us.csv')

# Encabezado mejorado
st.title('🚗 Análisis Exploratorio de Datos de Vehículos')
st.markdown('---')

# Información básica del dataset
st.subheader('📊 Información del Dataset')
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total de vehículos", len(car_data))
with col2:
    st.metric("Marcas únicas", car_data['model'].nunique())
with col3:
    st.metric("Rango de años", f"{car_data['model_year'].min():.0f} - {car_data['model_year'].max():.0f}")

st.markdown('---')

# Sección de visualizaciones
st.subheader('📈 Visualizaciones Interactivas')

# Usar checkboxes en lugar de botones
show_histogram = st.checkbox('Mostrar histograma de odómetro')
show_scatter = st.checkbox('Mostrar gráfico de dispersión precio vs odómetro')

if show_histogram:
    st.write('**Distribución del kilometraje de los vehículos**')
    fig_hist = px.histogram(car_data, x="odometer", 
                           title="Distribución del Odómetro",
                           labels={'odometer': 'Kilometraje', 'count': 'Cantidad'})
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter:
    st.write('**Relación entre precio y kilometraje**')
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                           title="Precio vs Kilometraje",
                           labels={'odometer': 'Kilometraje', 'price': 'Precio ($)'})
    st.plotly_chart(fig_scatter, use_container_width=True)

# Filtros interactivos
st.sidebar.header('🔧 Filtros')
price_range = st.sidebar.slider('Rango de precio', 
                                int(car_data['price'].min()), 
                                int(car_data['price'].max()), 
                                (int(car_data['price'].min()), int(car_data['price'].max())))

# Filtrar datos
filtered_data = car_data[(car_data['price'] >= price_range[0]) & 
                        (car_data['price'] <= price_range[1])]

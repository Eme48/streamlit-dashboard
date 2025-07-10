import streamlit as st
from dashboard import VehiclesDashboard
from data_loader import load_data
import plotly.express as px

# =======================================
# Configuración general de la aplicación
# =======================================

st.set_page_config(page_title="Análisis de Vehículos", layout="wide")
st.title("Análisis interactivo de vehículos en EE. UU.")

# ===========================
# Carga inicial de los datos
# ===========================

car_data = load_data("vehicles_us.csv")

# ==========================
# Inicializar el dashboard
# ==========================

dashboard = VehiclesDashboard(car_data)

# ======================================
# Filtros interactivos y datos filtrados
# ======================================

filtered_data = dashboard.apply_filters()

# ======================================
# Visualizaciones del Dashboard
# ======================================

dashboard.show_histogram(filtered_data)
dashboard.show_scatter_plot(filtered_data)
dashboard.show_time_series(filtered_data)

# ======================================
# Exportación y previsualización
# ======================================

dashboard.export_filtered_data(filtered_data)

# ======================================
# Visualizaciones adicionales (checkboxes)
# ======================================

st.header("Visualizaciones adicionales")

if st.checkbox("Mostrar histograma básico (odómetro)"):
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox("Mostrar dispersión precio vs odómetro"):
    fig2 = px.scatter(car_data, x="odometer", y="price", color="type")
    st.plotly_chart(fig2, use_container_width=True)

# ======================================
# Breve interpretación de resultados
# ======================================

st.markdown("### 🔍 Breve interpretación de los resultados")
st.markdown("""
- La mayoría de los vehículos listados tienen un precio entre **$5,000 y $20,000**.
- Los modelos más recientes tienden a tener precios promedio más altos, como era de esperarse.
- Los tipos de vehículos más comunes en el dataset son **sedan** y **SUV**.
- Al aplicar los filtros interactivos puedes explorar segmentos específicos, como autos económicos o autos con transmisión automática.
""")
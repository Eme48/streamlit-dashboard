import streamlit as st
from dashboard import VehiclesDashboard
from data_loader import load_data

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
dashboard.show_geographic_map(filtered_data)

# ======================================
# Exportación y previsualización
# ======================================

dashboard.export_filtered_data(filtered_data)

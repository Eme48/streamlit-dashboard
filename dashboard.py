import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils.filters import (
    filter_by_year,
    filter_by_price,
    filter_by_state,
    filter_by_transmission,
    filter_by_type
)
from data_loader import load_data  # cuando lo tengamos listo
from utils import add_coordinates  # cuando lo tengamos listo

# ---------------------
# Carga inicial de datos
# ---------------------
@st.cache_data
def load_and_prepare_data():
    df = load_data()
    df = add_coordinates(df)
    return df

# -----------------
# Sidebar: Filtros
# -----------------
def render_filters(df):
    st.sidebar.header("Filtros")

    year_range = st.sidebar.slider("Año del modelo", int(df['model_year'].min()), int(df['model_year'].max()), (2010, 2022))
    price_range = st.sidebar.slider("Precio", int(df['price'].min()), int(df['price'].max()), (1000, 50000))
    selected_states = st.sidebar.multiselect("Estado", sorted(df['state'].unique()))
    selected_transmissions = st.sidebar.multiselect("Transmisión", sorted(df['transmission'].dropna().unique()))
    selected_types = st.sidebar.multiselect("Tipo de vehículo", sorted(df['type'].dropna().unique()))

    return {
        "year_range": year_range,
        "price_range": price_range,
        "states": selected_states,
        "transmissions": selected_transmissions,
        "types": selected_types
    }

# ---------------------------
# Aplicar filtros seleccionados
# ---------------------------
def apply_filters(df, filters):
    df = filter_by_year(df, filters['year_range'])
    df = filter_by_price(df, filters['price_range'])

    if filters['states']:
        df = filter_by_state(df, filters['states'])
    if filters['transmissions']:
        df = filter_by_transmission(df, filters['transmissions'])
    if filters['types']:
        df = filter_by_type(df, filters['types'])

    return df

# --------------------
# Visualizaciones
# --------------------
def render_histogram(df):
    st.subheader("Distribución de precios")
    fig, ax = plt.subplots()
    sns.histplot(df['price'], bins=30, ax=ax)
    st.pyplot(fig)

def render_scatter(df):
    st.subheader("Precio vs. Año del modelo")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='model_year', y='price', hue='type', alpha=0.6, ax=ax)
    st.pyplot(fig)

def render_time_series(df):
    st.subheader("Promedio de precios por año")
    series = df.groupby('model_year')['price'].mean()
    st.line_chart(series)

def render_map(df):
    st.subheader("Distribución geográfica")
    if 'latitude' in df.columns and 'longitude' in df.columns:
        st.map(df[['latitude', 'longitude']].dropna())
    else:
        st.warning("No hay coordenadas disponibles para mostrar el mapa.")

# --------------------
# Exportación a CSV
# --------------------
def export_csv(df):
    st.subheader("Exportar resultados")
    st.download_button(
        label="Descargar CSV",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name="filtered_vehicles.csv",
        mime="text/csv"
    )

# --------------------
# Main App
# --------------------
def main():
    st.title("Dashboard de Vehículos Usados")

    df = load_and_prepare_data()
    filters = render_filters(df)
    filtered_df = apply_filters(df, filters)

    st.markdown(f"### Total de vehículos mostrados: {len(filtered_df)}")
    st.dataframe(filtered_df)

    render_histogram(filtered_df)
    render_scatter(filtered_df)
    render_time_series(filtered_df)
    render_map(filtered_df)
    export_csv(filtered_df)

if __name__ == "__main__":
    main()

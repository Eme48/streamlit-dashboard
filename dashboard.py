import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils.filters import (
    filter_by_year,
    filter_by_price,
    filter_by_transmission,
    filter_by_type
)
from utils.utils import preprocess_data


class VehiclesDashboard:
    def __init__(self, df):
        self.df = preprocess_data(df)

    def apply_filters(self):
        st.sidebar.header("Filtros")

        year_range = st.sidebar.slider(
            "Año del modelo",
            int(self.df['model_year'].min()),
            int(self.df['model_year'].max()),
            (2010, 2020)
        )

        price_range = st.sidebar.slider(
            "Rango de precios",
            int(self.df['price'].min()),
            int(self.df['price'].max()),
            (1000, 50000)
        )

        transmissions = st.sidebar.multiselect(
            "Transmisión",
            sorted(self.df['transmission'].dropna().unique())
        )

        types = st.sidebar.multiselect(
            "Tipo de vehículo",
            sorted(self.df['type'].dropna().unique())
        )

        filtered_df = filter_by_year(self.df, year_range)
        filtered_df = filter_by_price(filtered_df, price_range)

        if transmissions:
            filtered_df = filter_by_transmission(filtered_df, transmissions)

        if types:
            filtered_df = filter_by_type(filtered_df, types)

        return filtered_df

    def show_histogram(self, df):
        st.subheader("Distribución de precios")
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.histplot(df['price'], bins=30, ax=ax)
        ax.set_xlabel("Precio")
        ax.set_ylabel("Frecuencia")
        fig.tight_layout()
        st.pyplot(fig)

    def show_scatter_plot(self, df):
        st.subheader("Precio vs Año del modelo")
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.scatterplot(data=df, x='model_year', y='price', hue='type', alpha=0.6, ax=ax)
        ax.set_xlabel("Año del modelo")
        ax.set_ylabel("Precio")
        fig.tight_layout()
        st.pyplot(fig)

    def show_time_series(self, df):
        st.subheader("Precio promedio por año")
        time_series = df.groupby('model_year')['price'].mean()
        st.line_chart(time_series)

    def export_filtered_data(self, df):
        st.subheader("Exportar datos filtrados")
        st.download_button(
            label="Descargar CSV",
            data=df.to_csv(index=False).encode('utf-8'),
            file_name="filtered_vehicles.csv",
            mime="text/csv"
        )

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from utils.filters import (
    filter_by_year,
    filter_by_price,
    filter_by_transmission,
    filter_by_type
)
from utils.utils import add_coordinates, preprocess_data


class VehiclesDashboard:
    def __init__(self, df: pd.DataFrame):
        """
        Inicializa el dashboard con un DataFrame y prepara los datos.

        Args:
            df (pd.DataFrame): Dataset original.
        """
        self.df = preprocess_data(df)
        self.df = add_coordinates(self.df)
        self.filters = None

    def apply_filters(self):
        """
        Renderiza los filtros en la barra lateral y filtra los datos.

        Returns:
            pd.DataFrame: DataFrame filtrado.
        """
        st.sidebar.header("Filtros")

        year_range = st.sidebar.slider(
            "Año del modelo",
            int(self.df["model_year"].min()),
            int(self.df["model_year"].max()),
            (2010, 2022),
        )

        price_range = st.sidebar.slider(
            "Precio",
            int(self.df["price"].min()),
            int(self.df["price"].max()),
            (1000, 50000),
        )

        selected_transmissions = st.sidebar.multiselect(
            "Transmisión", sorted(self.df["transmission"].dropna().unique())
        )

        selected_types = st.sidebar.multiselect(
            "Tipo de vehículo", sorted(self.df["type"].dropna().unique())
        )

        df_filtered = filter_by_year(self.df, year_range)
        df_filtered = filter_by_price(df_filtered, price_range)

        if selected_transmissions:
            df_filtered = filter_by_transmission(df_filtered, selected_transmissions)
        if selected_types:
            df_filtered = filter_by_type(df_filtered, selected_types)

        self.filters = {
            "year_range": year_range,
            "price_range": price_range,
            "transmissions": selected_transmissions,
            "types": selected_types,
        }

        return df_filtered

    def show_histogram(self, df: pd.DataFrame):
        """Muestra un histograma de precios."""
        st.subheader("Distribución de precios")
        fig, ax = plt.subplots()
        sns.histplot(df["price"], bins=30, ax=ax)
        st.pyplot(fig)

    def show_scatter_plot(self, df: pd.DataFrame):
        """Muestra un gráfico de dispersión Año vs Precio."""
        st.subheader("Precio vs. Año del modelo")
        fig, ax = plt.subplots()
        sns.scatterplot(
            data=df, x="model_year", y="price", hue="type", alpha=0.6, ax=ax
        )
        st.pyplot(fig)

    def show_time_series(self, df: pd.DataFrame):
        """Muestra un gráfico de línea con el promedio de precios por año."""
        st.subheader("Promedio de precios por año")
        series = df.groupby("model_year")["price"].mean()
        st.line_chart(series)

    def export_filtered_data(self, df: pd.DataFrame):
        """Permite exportar los datos filtrados a CSV."""
        st.subheader("Exportar resultados")
        st.download_button(
            label="Descargar CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="filtered_vehicles.csv",
            mime="text/csv",
        )

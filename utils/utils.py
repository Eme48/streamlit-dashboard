"""
utils.py

Funciones utilitarias para el procesamiento y análisis de datos de vehículos usados.
"""

import pandas as pd
from utils.state_coords import STATE_COORDS


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocesa el DataFrame original con los datos crudos.

    - Elimina duplicados.
    - Convierte columnas relevantes a tipos numéricos.
    - Elimina filas con valores faltantes críticos.
    - Convierte nombres de estados a título capitalizado.

    Retorna:
        pd.DataFrame: DataFrame limpio y listo para análisis.
    """
    df = df.drop_duplicates()
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['odometer'] = pd.to_numeric(df['odometer'], errors='coerce')
    df['model_year'] = pd.to_numeric(df['model_year'], errors='coerce')
    df['state'] = df['state'].str.title()

    df = df.dropna(subset=['price', 'odometer', 'model_year', 'state'])

    return df


def add_coordinates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega columnas de latitud y longitud al DataFrame basadas en el estado.

    Utiliza las coordenadas definidas en el módulo `state_coords.py`.

    Retorna:
        pd.DataFrame: DataFrame con columnas 'lat' y 'lon' agregadas.
    """
    df['lat'] = df['state'].map(lambda s: STATE_COORDS.get(s, {}).get('lat'))
    df['lon'] = df['state'].map(lambda s: STATE_COORDS.get(s, {}).get('lon'))
    return df

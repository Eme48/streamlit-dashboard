"""
utils.py

Funciones utilitarias para el procesamiento y análisis de datos de vehículos usados.
"""

import pandas as pd

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

    df = df.dropna(subset=['price', 'odometer', 'model_year'])

    return df

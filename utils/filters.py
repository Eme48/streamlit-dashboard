"""
Módulo de filtros para el dashboard de vehículos.

Este módulo contiene funciones que permiten filtrar un DataFrame
según distintos criterios: año, precio, estado, tipo de transmisión
y tipo de vehículo. También incluye una función para aplicar múltiples
filtros de forma combinada.

"""

import pandas as pd

def filter_by_year(df: pd.DataFrame, year_range: tuple) -> pd.DataFrame:
    """
    Filtra el DataFrame por un rango de años del modelo.

    Parámetros:
        df (pd.DataFrame): DataFrame original con la columna 'model_year'.
        year_range (tuple): Rango de años como (mínimo, máximo).

    Retorna:
        pd.DataFrame: DataFrame filtrado por año del modelo.
    """
    if 'model_year' not in df.columns:
        raise ValueError("La columna 'model_year' no existe en el DataFrame.")
    return df[(df['model_year'] >= year_range[0]) & (df['model_year'] <= year_range[1])]

def filter_by_price(df: pd.DataFrame, price_range: tuple) -> pd.DataFrame:
    """
    Filtra el DataFrame por un rango de precios.

    Parámetros:
        df (pd.DataFrame): DataFrame original con la columna 'price'.
        price_range (tuple): Rango de precios como (mínimo, máximo).

    Retorna:
        pd.DataFrame: DataFrame filtrado por precio.
    """
    if 'price' not in df.columns:
        raise ValueError("La columna 'price' no existe en el DataFrame.")
    return df[(df['price'] >= price_range[0]) & (df['price'] <= price_range[1])]

def filter_by_transmission(df: pd.DataFrame, transmissions: list) -> pd.DataFrame:
    """
    Filtra el DataFrame por tipos de transmisión.

    Parámetros:
        df (pd.DataFrame): DataFrame original con la columna 'transmission'.
        transmissions (list): Lista de transmisiones a incluir.

    Retorna:
        pd.DataFrame: DataFrame filtrado por transmisión.
    """
    if 'transmission' not in df.columns:
        raise ValueError("La columna 'transmission' no existe en el DataFrame.")
    return df[df['transmission'].isin(transmissions)]

def filter_by_type(df: pd.DataFrame, types: list) -> pd.DataFrame:
    """
    Filtra el DataFrame por tipos de vehículo.

    Parámetros:
        df (pd.DataFrame): DataFrame original con la columna 'type'.
        types (list): Lista de tipos de vehículo a incluir.

    Retorna:
        pd.DataFrame: DataFrame filtrado por tipo de vehículo.
    """
    if 'type' not in df.columns:
        raise ValueError("La columna 'type' no existe en el DataFrame.")
    return df[df['type'].isin(types)]

def apply_filters(
    df: pd.DataFrame,
    year_range: tuple = None,
    price_range: tuple = None,
    transmissions: list = None,
    types: list = None
) -> pd.DataFrame:
    """
    Aplica múltiples filtros al DataFrame de manera combinada.

    Parámetros:
        df (pd.DataFrame): DataFrame original.
        year_range (tuple, opcional): Rango de años (mín, máx).
        price_range (tuple, opcional): Rango de precios (mín, máx).
        states (list, opcional): Lista de estados.
        transmissions (list, opcional): Lista de transmisiones.
        types (list, opcional): Lista de tipos de vehículo.

    Retorna:
        pd.DataFrame: DataFrame filtrado según los criterios especificados.
    """
    if year_range:
        df = filter_by_year(df, year_range)
    if price_range:
        df = filter_by_price(df, price_range)
    if transmissions:
        df = filter_by_transmission(df, transmissions)
    if types:
        df = filter_by_type(df, types)
    return df

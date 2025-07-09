import pandas as pd
import os

def load_data(file_path="vehicles_us.csv") -> pd.DataFrame:
    """
    Carga el dataset de vehículos desde un archivo CSV.

    Parámetros:
        file_path (str): Ruta al archivo CSV.

    Retorna:
        pd.DataFrame: DataFrame con los datos cargados.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"El archivo {file_path} no fue encontrado.")

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        raise RuntimeError(f"Error al leer el archivo CSV: {e}")

    # Conversión de columnas importantes a los tipos correctos
    df['model_year'] = pd.to_numeric(df['model_year'], errors='coerce')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # Eliminar filas sin año o precio válido
    df = df.dropna(subset=['model_year', 'price'])

    return df

import pandas as pd
import numpy as np

#Función para eliminar columnas que no aportan nada al análisis porque todos sus valores son iguales
#¿Porque es importante? Porque las columnas que tienen valores repetidos no sirven para entrenar modelos, visualizar datos o generar insights porque no tiene variabilidad
#¿Como funciona? Utiliza la función nunique(). Esto devuelve un conteo de valores únicos por columna, incluyendo los NaN (por eso dropna=False).
#.loc es un método de pandas para seleccionar filas y columnas. : selecciona todas las filas. ... selecciona solo las columnas que cumplen una condición.
#df.nunique(dropna=False) > 1:se traduce a "Dame todas las filas (:) y solo las columnas donde el número de valores únicos sea mayor a 1."
def remove_constant_columns(df: pd.DataFrame) -> pd.DataFrame:
    return df.loc[:, df.nunique(dropna=False) > 1]

#Función para eliminar filas duplicadas
#¿Porque es importante? Porque las filas duplicadas no sirven para entrenar modelos, visualizar datos o generar insights porque no tiene variabilidad
#¿Como funciona? Utiliza la función drop_duplicates(). Esto devuelve un DataFrame sin filas duplicadas.
def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()

#Función para rellenar valores nulos automaticamente. Si la columna es númerica, rellena con la mediana. Si es categórica (texto/string), rellena con la moda.
#¿Porque es importante? Los NaN pueden causar errores o distorsionar el análisis, ya sea para calculos, visualizaciones, etc.
def fill_missing_values(df: pd.DataFrame, strategy='auto') -> pd.DataFrame:
    df_clean = df.copy()
    for col in df_clean.columns:
        if df_clean[col].isnull().any():
            if pd.api.types.is_numeric_dtype(df_clean[col]):
                df_clean[col] = df_clean[col].fillna(df_clean[col].median())
            else:
                df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])
    return df_clean
    
#Función que detecta columnas que están como texto y los convierte automaticamente a int, float o datetime.
def fix_column_types(df: pd.DataFrame) -> pd.DataFrame:
    df_clean = df.copy()
    for col in df_clean.columns:
        # Intentar convertir a numérico
        numeric_col = pd.to_numeric(df_clean[col], errors='coerce')

        # Si la conversión a numérico fue exitosa (no todos los valores son NaN)
        if numeric_col.notna().any():
            df_clean[col] = numeric_col
            continue

        # Si la conversión a numérico falló, intentar convertir la columna original a datetime
        try:
            datetime_col = pd.to_datetime(df_clean[col], errors='coerce')
            # Si la conversión a datetime fue exitosa
            if datetime_col.notna().any():
                df_clean[col] = datetime_col
        except (ValueError, TypeError):
            # Si ambas conversiones fallan, la columna se queda como está
            pass

    return df_clean
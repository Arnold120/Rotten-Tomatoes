import pandas as pd

df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")

print("Primeras 5 filas del DataFrame:")
print(df_movies.head())

print("\nTipos de datos antes de la conversión:")
print(df_movies.dtypes)

df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

print("\nTipos de datos después de la conversión:")
print(df_movies.dtypes)

missing_dates = df_movies['in_theaters_date'].isna().sum()
print(f"\nPelículas con fechas no reconocidas: {missing_dates}")
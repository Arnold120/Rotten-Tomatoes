import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")

df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

total_peliculas = len(df_movies)
print(f"Total de películas: {total_peliculas}")

calificaciones = df_movies['tomatometer_status'].value_counts()
print("\nDistribución de calificaciones:")
print(calificaciones)

plt.figure(figsize=(7, 7))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
calificaciones.plot.pie(
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    labels=calificaciones.index
)
plt.title('Distribución de clasificación por la crítica')
plt.ylabel('')
plt.tight_layout()
plt.show()

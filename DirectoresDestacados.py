import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv('Data/Rotten Tomatoes Movies.csv')

directores_conteo = df_movies['directors'].value_counts()

top_10_directors = directores_conteo.head(10)
top_10_director_names = top_10_directors.index.tolist()
df_top_10 = df_movies[df_movies['directors'].isin(top_10_director_names)].copy()

promedio_tomatometer = df_top_10.groupby('directors')['tomatometer_rating'].mean().sort_values(ascending=False)

plt.figure(figsize=(10,6))
plt.bar(promedio_tomatometer.index, promedio_tomatometer.values, color='skyblue', edgecolor='black', alpha=0.7)
plt.xticks(rotation=45, ha='right')
plt.title('Calificacion Promedio (Tomatometer) de los Top 10 Directores Mas Frecuentes', pad=20)
plt.ylabel('Director')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

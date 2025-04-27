import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")
df_movies_copy = df_movies.copy()

df_genres_exploded = df_movies_copy.assign(genre=df_movies_copy['genre'].str.split(',')).explode('genre')
df_genres_exploded['genre'] = df_genres_exploded['genre'].str.strip()

promedio_audiencia_por_genero = df_genres_exploded.groupby('genre')['audience_rating'].mean()
top10_generos = promedio_audiencia_por_genero.sort_values(ascending=False).head(10)

plt.figure(figsize=(10,8))
plt.pie(top10_generos, labels=top10_generos.index, autopct='%1.1f%%', startangle=140)
plt.title('Top 10 géneros con mejor promedio de valoración por audiencia', pad=30)
plt.axis('equal')
plt.show()

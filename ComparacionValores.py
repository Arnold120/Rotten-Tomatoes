import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")
df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

promedio_criticos = df_movies['tomatometer_rating'].mean()
promedio_audiencia = df_movies['audience_rating'].mean()

print(f"Promedio de valoración por críticos: {promedio_criticos:.2f}")
print(f"Promedio de valoración por audiencia: {promedio_audiencia:.2f}")

df_movies['rating_diff'] = df_movies['audience_rating'] - df_movies['tomatometer_rating']
plt.figure(figsize=(8, 8))
plt.hist(df_movies['rating_diff'].dropna(), bins=30, edgecolor='black', color='#20B2AA')
plt.axvline(0, color='red', linestyle='dashed', linewidth=2, label='Sin diferencia')

plt.title('Distribución, diferencias entre audiencia y críticos')
plt.xlabel('Diferencia (Audiencia - Críticos)')
plt.ylabel('Número de películas')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

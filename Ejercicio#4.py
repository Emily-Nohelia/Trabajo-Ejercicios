import pandas as pd
import matplotlib.pyplot as plt

#se define la ruta del archivo
df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")
print(df_movies.head())

# 1. Crear una copia del DataFrame original
df_movies_copy = df_movies.copy()

# 2. Dividir la columna 'genre' por comas y explotar la lista
df_genres_exploded = df_movies_copy.assign(
    genre=df_movies_copy['genre'].str.split(',')
).explode('genre')

# 3. Limpiar espacios en blanco en los géneros
df_genres_exploded['genre'] = df_genres_exploded['genre'].str.strip()

# 4. Calcular el promedio de audiencia por género
genre_avg_rating = df_genres_exploded.groupby('genre')['audience_rating'].mean()

# 5. Obtener los 10 géneros con mejor promedio de calificación
top_10_genres = genre_avg_rating.sort_values(ascending=False).head(10)

# 6. Crear gráfico de pastel
plt.figure(figsize=(8, 6))
plt.pie(top_10_genres, labels=top_10_genres.index, startangle=90)
plt.title('Top 10 películas con mejor promedio de valoración')
plt.axis('equal')  # Mantener forma circular
plt.tight_layout()
plt.show()

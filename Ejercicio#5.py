import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")
print(df_movies.head())

# Carga del Dataset
print(df_movies.dtypes)

#Ejercicio 5
#Cuenta cuántas películas ha dirigido cada director usando value_counts() en la columna directors.
#Muestra los 10 directores que aparecen con más frecuencia.
#Calcula el promedio de tomatometer_rating para las películas de solo estos 10 directores.
# Pista: Puedes filtrar el DataFrame original para incluir solo las filas de estos directores y
# luego usar groupby('directors')['tomatometer_rating'].mean().

# 1. Contar cuántas películas ha dirigido cada director
conteo_directores = df_movies['directors'].value_counts()

# 2. Obtener los 10 directores más frecuentes
top_10_directors = conteo_directores.head(10)
print("\nTop 10 directores con más películas:")
print(top_10_directors)

# 3. Filtrar las películas
top_10_director_names = top_10_directors.index.tolist()
df_top_10 = df_movies[df_movies['directors'].isin(top_10_director_names)].copy()

# 4. Calcular el promedio
promedio_tomatometro = df_top_10.groupby('directors')['tomatometer_rating'].mean().sort_values(ascending=False)

# 5. Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(promedio_tomatometro.index, promedio_tomatometro.values, color='orange', edgecolor='black')
plt.title("Calificación Promedio (Tomatometer) de los Top 10 Directores Más Frecuentes")
plt.ylabel("Calificación Promedio")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

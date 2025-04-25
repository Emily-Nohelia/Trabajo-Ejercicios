import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")
print(df_movies.head())

# Carga del Dataset
print(df_movies.dtypes)
# Número total de películas
total_de_peliculas = len(df_movies)
print(f"Número total de películas: {total_de_peliculas}")

# 8. Número total de películas
total_de_peliculas = len(df_movies)
print(f"\n8. Número total de películas en el dataset: {total_de_peliculas}")

# 10. Distribución de películas por tomatometer_status
distribucion_de_calificaciones = df_movies['tomatometer_status'].value_counts()
print("\n10. Distribución de películas por tomatometer_status:")
print(distribucion_de_calificaciones)

# se crea el gráfico circular
plt.figure(figsize=(6, 6))
distribucion_de_calificaciones.plot.pie(
    startangle=140,# Empieza desde arriba
    labels=distribucion_de_calificaciones.index,     # Etiquetas de cada sección
    shadow=False,                                 # Sin sombra (efecto 3D)
    autopct=None                                  # No mostrar porcentajes dentro del pastel
)

plt.title('Distribución de calificación por la crítica')
plt.ylabel('')  # Oculta la etiqueta del eje Y
plt.show()
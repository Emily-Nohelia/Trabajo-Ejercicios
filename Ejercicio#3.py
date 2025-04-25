import pandas as pd
import matplotlib.pyplot as plt

#se define la ruta del archivo
df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")
print(df_movies.head())

# 1. Calcular promedios
promedio_criticos = df_movies['tomatometer_rating'].mean()
promedio_audiencia = df_movies['audience_rating'].mean()

print(f"Promedio de valoración por críticos: {promedio_criticos:.2f}")
print(f"Promedio de valoración por audiencia: {promedio_audiencia:.2f}")

# 2. Crear nueva columna con la diferencia
df_movies['rating_diff'] = df_movies['audience_rating'] - df_movies['tomatometer_rating']

# 3. Crear histograma
plt.figure(figsize=(10, 8))

# Barras del histograma y sus colores
plt.hist(df_movies['rating_diff'], bins=30, color='mediumseagreen', edgecolor='black', alpha=0.8)

# Línea punteada roja en x=0
plt.axvline(0, color='red', linestyle='--', linewidth=2, label='Sin diferencia')

# Título y etiquetas
plt.title("Distribución, diferencias entre audiencia y críticos")
plt.xlabel("Diferencia (Audiencia - Críticos)")
plt.ylabel("Número de películas")
plt.legend()
plt.tight_layout()
plt.show()
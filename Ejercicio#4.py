
#Importar las librerías
import pandas as pd
import matplotlib.pyplot as plt

#Se define la ruta del archivo
df_movies= pd.read_csv("./Data/Rotten Tomatoes Movies.csv")

#Se crea una copia del DataFrame original
df_movies_copy=df_movies.copy()

#separar los géneros

df_genres_exploded = df_movies_copy.assign(
  genre=df_movies_copy['genre'].str.split(',')
).explode('genre')

print(df_movies_copy)
df_genres_exploded['genre'] = df_genres_exploded['genre'].str.strip()

#Calcular el promedio de audience_rating para cada género individual
promedio_audiencia_géneros= df_genres_exploded.groupby('genre')['audience_rating'].mean().sort_values(ascending=False)
print(promedio_audiencia_géneros)

# •	Muestra los 10 géneros con el promedio de calificación de audiencia más alto haciendo uso de un diagrama de pastel.
Top_10_generos= promedio_audiencia_géneros.head(10)
print(Top_10_generos)

#Propiedades del gráfico
plt.figure(figsize= (10,10))
plt.pie(Top_10_generos,labels=Top_10_generos.index, startangle=140)
plt.title("Top 10 géneros con mejor promedio de valoración")
plt.tight_layout()
plt.show()
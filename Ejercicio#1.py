import pandas as pd
import matplotlib.pyplot as plt

# 2. Leer el archivo CSV
df_movies = pd.read_csv("Rotten Tomatoes Movies.csv")

# 3. Mostrar las primeras filas del DataFrame para revisar su contenido
print(df_movies.head())

# 4. Verificar los nombres y tipos de datos de las columnas
print("\nTipos de datos antes de la conversión:")
print(df_movies.dtypes)

# 5. Convertir la columna 'in_theaters_date' al tipo datetime
df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

# 6. Verificar que la conversión fue exitosa (dtypes)
print("\nTipos de datos después de la conversión:")
print(df_movies.dtypes)

# 7. Mostrar si hubo valores no convertidos (NaT)
missing_dates = df_movies['in_theaters_date'].isna().sum()
print(f"\nPelículas con fechas no reconocidas: {missing_dates}")
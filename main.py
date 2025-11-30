import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
df = pd.read_csv("data.csv")

# Ver tipos de datos de las columnas
print(df.dtypes)

# Convertir la columna 'Datetime' a tipo datetime
df['Datetime'] = pd.to_datetime(df['Datetime'])

# Establecer la columna 'Datetime' como índice del DataFrame
df.set_index('Datetime', inplace=True)

# Función para convertir de grados Kelvin a Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Copiar el DataFrame original y nombrarlo df_celsius
df_celsius = df.copy()

# Convertir las temperaturas de cada ciudad de Kelvin a Celsius usando la función creada
for col in df_celsius.columns:
    df_celsius[col] = df_celsius[col].apply(kelvin_to_celsius)

# --- Análisis en Phoenix ---
# Temperatura mínima
min_temp = df_celsius['Phoenix'].min()
min_date = df_celsius['Phoenix'].idxmin()
print(f"El día con la temperatura mínima en Phoenix fue: {min_date}")
print("La temperatura mínima registrada en Phoenix fue de:", round(min_temp, 2), "°C")

# Temperatura máxima
max_temp = df_celsius['Phoenix'].max()
max_date = df_celsius['Phoenix'].idxmax()
print(f"El día con la temperatura máxima en Phoenix fue: {max_date}")
print("La temperatura máxima registrada en Phoenix fue de:", round(max_temp, 2), "°C")

# Temperatura promedio en 2016
phoenix_2016 = df_celsius['Phoenix']['2016']
mean_temp_2016 = phoenix_2016.mean()
print("La temperatura promedio durante 2016 en Phoenix fue de:", round(mean_temp_2016, 2), "°C")

# --- Gráfico ---
plt.figure(figsize=(20, 10))
plt.scatter(phoenix_2016.index, phoenix_2016.values, label='Phoenix', color='orange')
plt.title('Temperatura en Phoenix durante 2016')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid()
plt.savefig("temperatura_phoenix_2016.png")
plt.show()

# Exportar el DataFrame modificado a un nuevo archivo CSV
df_celsius.to_csv("temperatura_celsius.csv")



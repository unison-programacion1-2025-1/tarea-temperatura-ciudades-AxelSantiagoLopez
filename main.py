import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data.csv")


print(df.dtypes)


df['Datetime'] = pd.to_datetime(df['Datetime'])


df.set_index('Datetime', inplace=True)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


df_celsius = df.copy()


for col in df_celsius.columns:
    df_celsius[col] = df_celsius[col].apply(kelvin_to_celsius)

min_temp = df_celsius['Phoenix'].min()
min_date = df_celsius['Phoenix'].idxmin()
print(f"El día con la temperatura mínima en Phoenix fue: {min_date}")
print("La temperatura mínima registrada en Phoenix fue de:", round(min_temp, 2), "°C")


max_temp = df_celsius['Phoenix'].max()
max_date = df_celsius['Phoenix'].idxmax()
print(f"El día con la temperatura máxima en Phoenix fue: {max_date}")
print("La temperatura máxima registrada en Phoenix fue de:", round(max_temp, 2), "°C")


phoenix_2016 = df_celsius['Phoenix']['2016']
mean_temp_2016 = phoenix_2016.mean()
print("La temperatura promedio durante 2016 en Phoenix fue de:", round(mean_temp_2016, 2), "°C")


plt.figure(figsize=(20, 10))
plt.scatter(phoenix_2016.index, phoenix_2016.values, label='Phoenix', color='orange')
plt.title('Temperatura en Phoenix durante 2016')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid()
plt.savefig("temperatura_phoenix_2016.png")
plt.show()

df_celsius.to_csv("temperatura_celsius.csv")



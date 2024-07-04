import pandas as pd


df = pd.read_csv("spotter.csv", header=[0])

df['lat(min*1e5)'] = df['lat(min*1e5)'].astype(str).str.replace('-', '.', 1)

# Unir as colunas
df['lat_degree_decimal'] = df['lat(deg)'].astype(str) + df['lat(min*1e5)']


df['long(min*1e5)'] = df['long(min*1e5)'].astype(str).str.replace('-', '.', 1)

# Unir as colunas
df['long_degree_decimal'] = df['long(deg)'].astype(str) + df['long(min*1e5)']

# Transformar a nova coluna em float (opcional, dependendo do que você precisa)
# df['coluna_unida'] = df['coluna_unida'].astype(float)

df = df.drop(['long(min*1e5)', 'long(deg)', 'lat(deg)', 'lat(min*1e5)'], axis=1)

# Mostrar o resultado
print(df)

df.to_csv('new_spotter.csv', index=False)
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('titanic.csv')

print(df.head())

print(df.info())

print(df.describe())

# Datatypes
print(df.dtypes)

# Filtro
print(df[df['age'] >= 10].head())

# Retorna as linhas duplicadas
duplacateRows = df[df.duplicated()]
print(duplacateRows)

print(len(df))

df.drop_duplicates(keep='last', inplace=True)

print(len(df))

# Remoção de valores nulos
df.dropna(subset=['deck'], inplace=True)

print(df)

# Substituindo NaN por zero
df.replace(np.nan, '0', inplace=True)
print(df)

# Renomear colunas
df = df.rename(columns={'sex': 'Genero'})

print(df.head(5))

# Métodos de coordenação
sorted_df = df.sort_values(by='Genero', ascending=True)

print(sorted_df)

# Groupby
grouped_by = df.groupby('age').mean

print(grouped_by.head())

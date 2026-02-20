import pandas as pd

data = {
    'Nome':['Vanessa', 'Irlan', 'Bernardo', 'Louise'],
    'Idade':[34, 35, 2, 4],
    'Cidade':['Armazén', 'Castahal', 'Floripa', 'São José']
}

df = pd.DataFrame(data)

print(df)

# Acessa linha 'Nome'
print(df['Nome'])

# Acessando uma linha
print(df.iloc[0])

# Acessa um valor específico
print(df.loc[0, 'Nome'])
import pandas as pd

funcionarios = {
    'Nome':['Vanessa', 'Irlan', 'Bernardo'],
    'Endereço':['Rua Bartolomeu da Silva', 'Rua João Alexandre da Silva', 'Rua João Alexandre da Silva'],
    'Data de Nascimento':['16-03-1992', '20-05-1991', '29-02-2024'],
    'Data de Admissão':['18-01-2014', '20-03-2019', '09-02-2026'],
    'Salário':[7800, 3000, 1200],
    'Cargo':['Cientista de Alimentos', 'Analista de Sistemas', 'Jovem Aprendiz']
}

df = pd.DataFrame(funcionarios)

print(df)

print(df['Data de Admissão'])
import matplotlib.pyplot as plt

# Dados
x = ['Maça', 'Laranja', 'Uva', 'Banana', 'Figo']
y = [5, 3, 7, 4, 6,]

plt.bar(x, y, color ='green') # Imprime um grafico em barras na cor verde

# Adicionando rótulos
plt.xlabel('Frutas')
plt.ylabel('Quantidade')
plt.title('Quantidade de Frutas') # Título do grafico

plt.show() # Exibe um gráfico de barras
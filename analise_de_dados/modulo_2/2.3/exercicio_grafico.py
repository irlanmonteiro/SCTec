import matplotlib.pyplot as plt

# Dados
x = ['Vanessa', 'Irlan', 'Bernardo']
y = [7800, 3000, 1200]

plt.bar(x, y, color = 'blue')

# Adicionando rótulos
plt.xlabel('Funcionários')
plt.ylabel('Salário (R$)')
plt.title('Gráfico de Salário') # Título do grafico

plt.show()
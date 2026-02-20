import numpy as np

# Matriz 3x3 com índice (0,1,2)
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr2[1, 2]) # Saída espera: 6

# Informações da matriz
print(f'Shape da matriz: {arr2.shape}')
print(f'Número de elementos: {arr2.size}')
print(f'Tipo de elementos: {arr2.dtype}')

# Operações matemáticas

arr1 = np.array([10, 20, 30, 40, 50])

print(arr1 + 10) # Soma + 10 aos elementos

print(arr2 * 2) # Cada elemento interno da matriz foi multiplicao por 2

print('Média')
print(np.mean(arr1)) # Calcula oa média dos  elementos

print('Mediana')
print(np.median(arr1)) # Calcula o valor que está no meio quando os dados são ordenados

print('Desvio padrão') # Calcula a dispersão dos dados
desvio_padrao = np.std(arr1)
print((desvio_padrao))

print('Variância') # Calcula o quadrado do desvio padrão
variancia = np.var(arr1)
print(variancia)

min = np.min(arr1)
max = np.max(arr1)

print(f'Mínimo: {min}') # Exibe o Minimo do array
print(f'Máximo: {max}') # Exibe o Maximo do array
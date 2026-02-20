# Pedindo os números ao usuário e convertendo para inteiro
inicio = int(input('Esse app vai mostrar todos os números pares entre 2 números. Para isso, digite o primeiro número:'))
fim = int(input('Digite o último número:'))

print(f"\nNúmeros pares entre {inicio} e {fim}:")

# O range vai do início até o fim + 1 (para incluir o último número se ele for par)
for numero in range(inicio,fim + 1):
    # O operador % (módulo) pega o resto da divisão. Se for 0, o número é par.
    if numero % 2 == 0:
        print(numero)
   
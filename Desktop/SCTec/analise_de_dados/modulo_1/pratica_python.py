nome = input("Digite seu nome:")
# Usamos f" no início para que o Python entenda o que está entre { }
print(f"Olá {nome}, agora vamos calcular quantos anos você terá em 2030!")

# Precisamos transformar a entrada em número usando int()
idade = int(input("Digite sua idade:"))

# Cálculo: sua idade hoje + os 4 anos que faltam para 2030
ano_2030 = idade + 4

print(f"Você terá {ano_2030} anos em 2030!")
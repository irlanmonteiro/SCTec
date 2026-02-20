telefones = ["1234-5678","2222-2222","7777-7777","9999-9999"]
print(telefones)

#append(): Adiciona o item ao final da lista.
telefones.append("5555-5555")
print(telefones)

#insert(índice, valor): Adiciona o item em uma posição específica, no caso indice 0.
telefones.insert(0,"3333-3333")
print(telefones)

#remove(valor): Remove a primeira ocorrência de um valor específico.
telefones.remove("3333-3333")
print(telefones)

#pop(índice): Remove o item que está em uma posição (índice) determinada.
telefones.pop(1)
print(telefones)

contato = ["nery, 7485-9632"]

#Lista vazia
telefones2 = []

# Adiciona a lista 'contato' como um único elemento dentro de 'telefones2'.
telefones2.append(contato)

print(telefones2)

# Tranforma a lista em tuplas: [(nome, numero)]
telefones3 = [("nery","7485-9632"),("Van","9483-3861"),("Bê","3561-4562")]
print(telefones3)

# Tranforma a lista Telefones3 em Dicionário
telefones3_dict = dict(telefones3)
print(telefones3_dict)

# Imprime o valor de Nery
print(telefones3_dict["nery"])

# Adiciona Paulo e Numero com Tupla: [(chave, valor)] ao final da lista
telefones3_dict["Paulo"] = "3456-7899"
print(telefones3_dict)

#Remove Paulo do Dicionário
telefones3_dict.pop("Paulo")
print(telefones3_dict)
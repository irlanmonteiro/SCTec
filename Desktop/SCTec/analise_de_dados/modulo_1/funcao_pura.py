def pure_increments(elements,index):
    """
    Incrementa um valor em uma lista de forma pura (sem efeito colateral).

    Cria uma nova lista baseada na original, altera o valor no índice 
    especificado e retorna essa nova lista, mantendo a original intacta.

    Args:
        elements (list): A lista original de elementos (ex: números).
        index (int): A posição (índice) do elemento que deve ser incrementado.

    Returns:
        list: Uma nova lista com o elemento incrementado.
    """
    new_elements = elements.copy() # Cria uma cópia rasa (shallow copy) para não alterar a referência original
    new_elements[index] += 1 # Incrementa o valor na posição desejada dentro da cópia
    return new_elements

lista = [1,2,3,4,5,6,7,8,9]

# Chama a função e imprime o resultado (a nova lista alterada)
print(pure_increments(lista,0)) 

# Imprime a lista original para provar que ela não sofreu alterações
print(lista) 
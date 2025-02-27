'''Escreve uma função em Python que, dada uma lista de elementos, 
devolvaessa mesma lista, mas sem elementos repetidos.'''

def remover_repetidos(lista):
    return list(set(lista))

# Exemplo de uso
lista = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6]
print("Lista sem repetidos:", remover_repetidos(lista))

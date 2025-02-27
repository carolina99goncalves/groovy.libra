def remover_repetidos_ordenado(lista):
    lista_sem_repetidos = []
    for elemento in lista:
        if elemento not in lista_sem_repetidos:
            lista_sem_repetidos.append(elemento)
    return lista_sem_repetidos

# Exemplo de uso
lista = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6]
print("Lista sem repetidos (mantendo a ordem):", remover_repetidos_ordenado(lista))
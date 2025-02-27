'''Escreve uma função em Python que dada uma lista de números imprime a somados valores dessa lista, 
o número de elementos da lista e a media desses valores.'''

def analisar_lista(numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade if quantidade > 0 else 0  # Evita divisão por zero

    print(f"Soma dos valores: {soma}")
    print(f"Número de elementos: {quantidade}")
    print(f"Média dos valores: {media:.2f}")

# Exemplo de uso
numeros = list(map(float, input("Digite os números separados por espaço: ").split()))
analisar_lista(numeros)
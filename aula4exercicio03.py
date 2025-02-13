'''Escreve um programa que devolve todos os numeros entre 100 e 200 (exclusive), divisiveis por 3'''

# Percorre os números de 100 a 199 (200 é exclusivo)
for numero in range(100,200):
    if numero % 3 == 0:  # Verifica se é divisível por 3
        print(numero)
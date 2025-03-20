'''1. Leia uma cadeia de caracteres no formato “DD/MM/AAAA” e copie o dia, mês e ano para três variáveis inteiras. '''

data = input("Digite a data no formato DD/MM/AAAA: ")

dia, mes, ano = map(int, data.split('/'))

print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")


'''2. Escreve uma função em Python que dada uma palavra retorne o número de vogais nessa palavra. '''

def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = sum(1 for letra in palavra if letra in vogais)
    return contador

palavra = input("Escreve uma palavra: ")
print(f"Número de vogais: {contar_vogais(palavra)}")


'''3. Escreve uma função em Python que dada uma lista de números imprime a soma dos valores dessa lista,
o número de elementos da lista e a media desses valores. Implementa tratamento de exceções no teu código 
(try…except…else..finally).'''

def processar_lista(lista):
    try:
        soma = sum(lista)  # Calcula a soma dos números
        quantidade = len(lista)  # Conta os elementos da lista
        media = soma / quantidade  # Calcula a média
    except ZeroDivisionError:
        print("Erro: A lista está vazia, não é possível calcular a média.")
    except TypeError:
        print("Erro: A lista deve conter apenas números.")
    else:
        print(f"Soma: {soma}, Quantidade: {quantidade}, Média: {media}")
    finally:
        print("Execução finalizada.")

# Exemplo de uso:
lista_numeros = [10, 20, 30, 40, 50]
processar_lista(lista_numeros)


'''Utilizando a biblioteca NumPy : 
a. Cria um array de números 1 com shape (8, 2) 
b. Cria um array de zeros com shape (5, 7) 
c. Subtraia o novo array de outro com dados aleatórios e armazene o numa variável 
chamada subarray 
d. Calcula a média dos valores do array subarray '''

import numpy as np

# a. Criar um array de números 1 com shape (8, 2)
array_ones = np.ones((8, 2))
print("Array de 1s:\n", array_ones)

# b. Criar um array de zeros com shape (5, 7)
array_zeros = np.zeros((5, 7))
print("\nArray de 0s:\n", array_zeros)

# c. Criar um array aleatório e subtrair de outro array, armazenando o resultado em subarray
array_random = np.random.rand(5, 7)  
subarray = array_zeros - array_random  
print("\nSubarray (zeros - aleatório):\n", subarray)

# d. Calcular a média dos valores do array subarray
media_subarray = np.mean(subarray)
print("\nMédia dos valores do subarray:", media_subarray)



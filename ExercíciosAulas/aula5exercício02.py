'''Escreva uma programa que, dada uma string representando um texto, imprima o numero de palavras existentes.
Observação: voce deve remover os sinais de pontuação (".", ",". ":", ";", "!" e "?") antes de realizar
a contagem das palavras'''

import string

# Entrada do usuário
texto = input("Digite um texto: ")

# Remover pontuação
for pontuacao in string.punctuation:
    texto = texto.replace(pontuacao, "")

# Dividir a string em palavras
palavras = texto.split()

# Contar as palavras
quantidade_palavras = len(palavras)

# Exibir o resultado
print(f"Número de palavras: {quantidade_palavras}")
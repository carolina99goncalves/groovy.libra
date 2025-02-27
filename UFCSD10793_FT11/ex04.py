'''Escreve uma função em Python que dada uma palavra retorne o número de vogais nessa palavra.'''

def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = sum(1 for letra in palavra if letra in vogais)
    return contador

# Exemplo de uso
palavra = input("Digite uma palavra: ")
print(f"A palavra '{palavra}' contém {contar_vogais(palavra)} vogais.")
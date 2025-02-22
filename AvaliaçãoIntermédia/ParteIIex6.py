'''Cria ou faz download de um ficheiro CSV. 
De seguida cria um programa que leia o ficheiro CSV e mostre cada linha do mesmo.'''

import csv  
import os  

# Caminho completo do ficheiro
caminho_ficheiro = r"C:\Users\10680\OneDrive - EFACEC Power Solutions, SGPS, SA\Desktop\FundamentosPython_VSC\AvaliaçãoIntermédia\exercício06.csv"


# Verifica se o ficheiro existe antes de tentar abrir
if os.path.exists(caminho_ficheiro):  
    with open(caminho_ficheiro, "r", encoding="utf-8") as ficheiro:  
        print("Conteúdo do ficheiro:\n")  
        print(ficheiro.read())  

    # Reabrir o ficheiro para ler com csv.reader()  
    with open(caminho_ficheiro, newline='', encoding="utf-8") as ficheiro:  
        leitor_csv = csv.reader(ficheiro)  
        print("\nConteúdo formatado como lista:")
        for linha in leitor_csv:  
            print(linha)  
else:  
    print("Erro: o ficheiro não foi encontrado")  
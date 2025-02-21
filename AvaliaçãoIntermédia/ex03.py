'''Verifique se um ficheiro existe antes de o abrir.'''

import os 
try: 
    caminho = input("Digite o caminho do ficheiro: ")
    
    if os.path.exists(caminho):
        with open(caminho, "r") as ficheiro:
            print(ficheiro.read())
    else:
        print("Erro: O ficheiro não foi encontrado")
except Exception as e: 
    print("Erro inesperado:", e)
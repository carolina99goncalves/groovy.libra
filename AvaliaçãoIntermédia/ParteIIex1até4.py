"""1. Cria um programa que leia um ficheiro de texto e exiba o seu conteúdo"""

with open("exemplo.txt", "r") as ficheiro: 
    conteudo = ficheiro.read() 
    print(conteudo)
    

"""2.Modifica o exercício anterior para exibir o conteúdo linha por linha."""

with open("exemplo.txt", "r") as ficheiro: 
    for linha in ficheiro: 
        print(linha.strip())
        
"""3. Cria um programa que escreva três linhas num ficheiro novo."""

with open("novo_ficheiro.txt", "w") as ficheiro: 
    ficheiro.write("Linha 1") 
    ficheiro.write("Linha 2") 
    ficheiro.write("Linha 3")
    
"""4. Modifica o programa anterior para acrescentar mais uma linha ao ficheiro."""

with open("novo_ficheiro.txt", "a") as ficheiro: 
    ficheiro.write("Linha adicional")
    


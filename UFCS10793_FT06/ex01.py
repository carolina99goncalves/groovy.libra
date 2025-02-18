"""Considera a lista:
cores=["amarelo", "azul", "branco", "preto", "verde"]
Cria um programa, em python, que:"""

#a faz o print de toda a lista
cores=["amarelo", "azul", "branco", "preto", "verde"]
print(cores)

#Faz o print do indíce 2 da lista
print(cores[2])

#Altera o indíce 0 da lista para "vermelho"
cores[0]='vermelho' 
print(cores)

#Faz o print de toda a lista
print(cores)

#Acrescenta no final da lista a cor "amarelo"
cores.append("amarelo")
print(cores)

#Acrescenta no indíce 2 a cor "roxo"
cores.insert(2, "roxo")
print(cores)


#Apaga o último elemento da lista
cores.pop()
print(cores)

#Faz o print do tamanho da lista (len)
print(len(cores))


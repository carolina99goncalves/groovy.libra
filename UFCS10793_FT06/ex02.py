"""Considera a lista: notas=[11.2, 15, 8.7, 17.2, 7.9 ]"""

notas=[11.2, 15, 8.7, 17.2, 7.9 ]
#Acrescenta o valor 10.9 no final da lista e faz o print de toda a lista
notas.append(10.9)
print(notas) 

#Faz o print do tamanho da lista
print(len(notas))

#Faz o print do valor mínimo da lista
print(min(notas))

#Faz a média dos valores da lista
media=sum(notas)/len(notas)
print(f"A média das notas é: {media: .2f}")




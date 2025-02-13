#Crie um programa para controlar listas, com as seguintes funções:
#Adicionar elemento no início;
#Adicionar elemento no fim;
#Remover elemento;
#Tamanho da lista;
#Imprimir elementos da lista;
#Esvaziar lista;

lista=[1,2,3,4,5,6,7,8,9,10,11,12]

lista.insert(0,8)
print(lista) #Adicionar elemento no início;

lista.append(8)
print(lista) #Adicionar elemento no fim;

lista.remove(8)
print(lista) #Remover elemento;

print(len(lista)) #Tamanho da lista;

print(sum(lista)) #Imprimir elementos da lista;

lista.clear()
print(lista) #Esvaziar lista


import copy

'''Efetua um programa em python:
a.Instancie o seguinte dicionário:
Computadores_1={
"Marca":"Asus",
"Ecra":"14Pol",
"RAM": [4, 8, 12]
}'''

# a) Cria um dicionário e faz print
Computadores_1={
"Marca":"Asus",
"Ecra":"14Pol",
"RAM": [4, 8, 12]
}
print("computador:", Computadores_1)

#b.Acrescente um novo elemento à lista com chave igual a “Disco” e valor [“128G”, “256G”]
Computadores_1["Disco"] = ["128G","256GB"]
print("\nDicionário atualizado:", Computadores_1)

#c.Permita ao utilizador introduzir um valor específico de RAM e verificar se esta está presente na lista.
ram_procurada = int(input("Introduza um valor de RAM para verificar se está na lista: "))

if ram_procurada in Computadores_1["RAM"]:
    print(f"O valor {ram_procurada}GB está disponível na lista de RAM.")
else:
    print(f"O valor {ram_procurada}GB não está na lista de RAM.")
    
#d.Acrecente 16 como novo valor de RAM.
Computadores_1["RAM"].append(16)

# Mostrar o dicionário atualizado
print("\nDicionário atualizado:", Computadores_1)

#e.Copie o dicionário para um novo usando Deep Copy().
Computadores_2 = copy.deepcopy(Computadores_1)

#ou

Computadores_2 = Computadores_1.copy()

# Mostrar os dois dicionários para confirmar a cópia
print("\nDicionário original:", Computadores_1)
print("Dicionário copiado (Deep Copy):", Computadores_2)

#f.No novo dicionário modifique a marca para “Lenovo” e os valores da RAM para [4,8]. 
Computadores_2["Marca"] = "Lenovo"
Computadores_2["RAM"] = [4, 8]

#Imprima a nova lista
print("\nNovo dicionário modificado (Computadores_2):", Computadores_2)

#g.Crie uma nova lista com deep copy e modifique a marca para “HP” e Disco para [“256G”]
Computadores_3 = copy.deepcopy(Computadores_1)
Computadores_3["Marca"] = "HP"
Computadores_3["Disco"] = ["256G"]

# Imprimir o novo dicionário modificado
print("\nNovo dicionário modificado (Computadores_3):", Computadores_3)

#h.Cria uma lista cujos elementos são os três dicionários.
lista_computadores = [Computadores_1, Computadores_2, Computadores_3]

# Imprimir a lista para verificar se os três dicionários estão dentro dela
print("\nLista de dicionários:")
for idx, computador in enumerate(lista_computadores, start=1):
    print(f"Computador {idx}: {computador}")

#i.Imprima as marcas com 128G de Disco
print("\nMarcas com 128G de Disco:")

for computador in lista_computadores:
    if "Disco" in computador and "128G" in computador["Disco"]:
        print(computador["Marca"])

# j.Imprima as marcas com 8 e 12 de RAM
print("\nMarcas com 8 e 12 de RAM:")

for computador in lista_computadores:
    if "RAM" in computador and 8 in computador["RAM"] and 12 in computador["RAM"]:
        print(computador["Marca"])
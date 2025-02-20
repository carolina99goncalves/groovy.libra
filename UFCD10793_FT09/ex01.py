"1.Considera o seguinte dicionário, a que cada prato é associado o respetivo valor em euros"
menu={
"entremeada": 7,
"Sardinha": 6,
"Filetes": 5.5,
"Prego": 7,
"Hamburguer": 5.5
}

#Dicionário com os pratos e seus preços
menu = {
    "entremeada": 7,
    "Sardinha": 6,
    "Filetes": 5.5,
    "Prego": 7,
    "Hamburguer": 5.5
}

# a) Devolve o preço do "Prego"
preco_prego = menu["Prego"]
print(f"O preço do Prego é: {preco_prego} euros")

# b) Faz o print de todas as chaves do dicionário (nomes dos pratos)
print("Os pratos disponíveis no menu são:")
for prato in menu.keys():
    print(prato)
    
# c) Acrescenta "omolete" com o preço de 5 euros
menu["omolete"] = 5

# d) Faz o print do dicionário atualizado
print("\nMenu atualizado:")
for prato, preco in menu.items():
    print(f"{prato}: {preco} euros")
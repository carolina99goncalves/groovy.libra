print("a - Cria um dicionário e efetua o respetivo print")
print("b - Acrescentes dois novos elementos ao dicionário")
print("c - Removes um dos elementos da lista")
print("d - Efetues uma operação, à escolha, sobre os dados no dicionário")
disciplinas = {"matematica":15, "ingles":16, "historia":16}
while True:
    user = input("Escolha uma opção:")
    match user:
        case "a":
            print(disciplinas)
        case "b":
            disciplinas.update({"portugues":15})
            disciplinas.update({"geografia":15})
            print(disciplinas)
        case "c":
            del disciplinas["matematica"]
            print(disciplinas)
        case "d":
            disciplinas.popitem()
            print("Removi o último conjunto chave:valor")
            print(disciplinas)
        case _:
            print("Escolha uma opção entre a e d")
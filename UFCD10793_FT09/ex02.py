"""Efetua um programa em python onde:
a.Cries um dicionário e efetues o respetivo print.
b.Acrescentes dois novos elementos ao dicionário.
c.Removes um dos elementos da lista;
d.Efetues uma operação, à escolha, sobre os dados no dicionário"""

# a) Cria um dicionário e faz print
dados = {
    "nome": "João",
    "idade": 25,
    "cidade": "Lisboa"
}
print("Dicionário inicial:", dados)

# b) Acrescentar dois novos elementos
dados["profissão"] = "Engenheiro"
dados["salário"] = 2000
print("\nDicionário após adicionar elementos:", dados)

# c) Remover um elemento (por exemplo, a cidade)
del dados["cidade"]
print("\nDicionário após remover um elemento:", dados)

# d) Efetuar uma operação (exemplo: aumentar o salário em 10%)
dados["salário"] *= 1.10
print("\nDicionário após aumentar o salário:", dados)
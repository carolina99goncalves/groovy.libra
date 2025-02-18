# Lista inicial
nums = [10, 2.5, 7, 11, 7.9, "Python", True, 6, 5.8, "Listas"]
# a. Conta a quantidade de cada tipo de dado
inteiros = len([x for x in nums if isinstance(x, int) and not isinstance(x, bool)])
floats = sum(1 for x in nums if isinstance(x, float))
strings = sum(1 for x in nums if isinstance(x, str))
booleanos = sum(1 for x in nums if isinstance(x, bool))
print(f"Inteiros: {inteiros}, Floats: {floats}, Strings: {strings}, Booleanos: {booleanos}")
# b. Calcula a média dos inteiros
valores_inteiros = [x for x in nums if isinstance(x, int) and not isinstance(x, bool)]
media = sum(valores_inteiros) / len(valores_inteiros)
print(media)
# c. Cria uma nova lista só com os inteiros
lista_inteiros = [x for x in nums if isinstance(x, int) and not isinstance(x, bool)]
print(lista_inteiros)
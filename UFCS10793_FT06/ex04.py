"""Considera a seguinte lista: nums=[10, 2.5, 7, 11, 7.9, "Python", True,6, 5.8 , "Listas"]"""
#Imprima a quantidade de inteiros, floats, strings e boleanos na lista;
#Efetua a média de todos os valores inteiros na lista.
#Crie e retorne uma nova lista só com os valores inteiros 

# Lista 
nums = [10, 2.5, 7, 11, 7.9, "Python", True, 6, 5.8, "Listas"]

# Contadores para os tipos de dados
qtd_inteiros = 0
qtd_floats = 0
qtd_strings = 0
qtd_booleanos = 0

# Lista para armazenar apenas inteiros
inteiros = []

# Soma dos inteiros para calcular a média
soma_inteiros = 0

# Iterar pela lista para classificar os elementos
for item in nums:
    if isinstance(item, int) and not isinstance(item, bool):  # Evita contar True como inteiro
        qtd_inteiros += 1
        soma_inteiros += item
        inteiros.append(item)
    elif isinstance(item, float):
        qtd_floats += 1
    elif isinstance(item, str):
        qtd_strings += 1
    elif isinstance(item, bool):
        qtd_booleanos += 1

# Calcular a média dos inteiros (evita divisão por zero)
media_inteiros = soma_inteiros / qtd_inteiros if qtd_inteiros > 0 else 0

# Exibir os resultados
print(f"Quantidade de inteiros: {qtd_inteiros}")
print(f"Quantidade de floats: {qtd_floats}")
print(f"Quantidade de strings: {qtd_strings}")
print(f"Quantidade de booleanos: {qtd_booleanos}")
print(f"Média dos valores inteiros: {media_inteiros:.2f}")
print(f"Lista apenas com inteiros: {inteiros}")

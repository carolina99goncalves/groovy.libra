nums = [10, 2.5, 7, 11, 7.9, "Python", True, 6, 5.8, "Listas"]
# a. Calcula e Imprime a quantidade de inteiros, floats, strings e boleanos na lista
int_count = sum(isinstance(x, int) and not isinstance(x,bool) for x in nums)
float_count = sum(isinstance(x, float) for x in nums)
str_count = sum(isinstance(x, str) for x in nums)
bool_count = sum(isinstance(x, bool) for x in nums)
print(f"Quantidade de inteiros: {int_count}")
print(f"Quantidade de floats: {float_count}")
print(f"Quantidade de strings: {str_count}")
print(f"Quantidade de booleanos: {bool_count}")

# b. Efetua a média de todos os valores inteiros na lista
int_values = [x for x in nums if isinstance(x, int) and not isinstance(x,bool)]
if int_values:
    int_mean = sum(int_values) / len(int_values)
    print(f"Média dos valores inteiros: {int_mean}")
else:
    print("Não há valores inteiros na lista para calcular a média.")
# c. Crie e retorne uma nova lista só com os valores inteiros
int_list = [x for x in nums if isinstance(x, int)and not isinstance(x,bool)]
print(f"Nova lista com valores inteiros: {int_list}")
'''Escreve um programa que solicite um número inteiro ao utilizador e caso o mesmo seja maior que 20, 
devolva o resultado da sua divisão por 2.'''

num = int(input("Digite um número: "))
if num > 20:
    print(f"O resultado da divisão de {num} por 2 é {num / 2}")
else:
    print("O número digitado é menor ou igual a 20")
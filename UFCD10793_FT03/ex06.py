'''Escreve um programa que receba três números reais e indique qual o maior dos três números.'''

# Solicita três números reais ao utilizador
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verifica qual número é o maior
if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

# Exibe o maior número
print(f"O maior número é {maior}.")
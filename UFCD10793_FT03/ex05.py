'''Escreva um programa que verifique se um determinado número introduzido pelo utilizador é nulo, 
positivo ou negativo.'''

# Solicita um número ao utilizador
numero = float(input("Digite um número: "))

# Verifica se o número é positivo, negativo ou nulo
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é nulo.")

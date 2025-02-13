'''Escreve um programa que calcule a soma e o produto dos N primeiros números naturais.'''

soma=0  # Variável para armazenar a soma
produto=1  # Variável para armazenar o produto
x= input("Introduza um número para calcular a soma: ")
x= int(x)
for i in range(1,x+1):  # Vai de 1 até X
    soma += i # Soma dos números
    produto *= i  # Produto dos números
    
print(soma)
print(produto)
#Impletemente uma calculadora simples com as operações aritméticas básicas. O utilizador deverá especificar a operação desejada (+,-,*,/) e, em seguida, inserir dois valores.
#Caso o utilizador escolha divisão e insira como valor do denominador 0 mostra uma mensagem personalizada. Para os restantes casos, mostra no ecrã o resultado da operação desejada.
operação = input("Operação:")
n1 = float(input("N1:"))
n2 = float(input("N2:"))
if operação == "+":
    print(n1+n2)
elif operação == "-":
    print(n1-n2)
elif operação == "*":
    print(n1*n2)
elif operação == "/":
    if n2 == 0:
        print("Não pode dividir um número por 0")
    else:
        print(n1/n2)
else:
    print("Operação inválida")
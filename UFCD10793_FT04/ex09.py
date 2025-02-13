'''Reescreve o programa anterior de forma a apresentar a tabuada de qualquer númerointroduzido pelo utilizador.'''

numero = int(input("Digite o número para cálcular a tabuada\n---->\t"))
for x in range (1,11):
    multiplicacao = numero * x
    print (f"{numero}*{x}={multiplicacao}\n")
    
    
#outra resoluçao
x = input('introduza o valor a multiplicar')
for i in range(1, 11):
    print(int(x), 'x', i, '=', int(x) * i)
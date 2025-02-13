#Escreva um programa que imprima os números de 1 até 50.

for num in range(1,51):
    print(num)

#Utilizando estruturas de repetição escreva um programa que mostre os resultados 
#da tabuada de multiplicação dos números entre 1 e 10, como segue

for num in range(1,11):
    for num2 in range(1,11):
        print(f'{num} x {num2} = {num*num2}')
        
#Escreva um programa que gere 100 números reais aleatórios entre 0 e 1 e armazene os numa lista. No final 
# o programa deverá mostrar as seguintes informações:
#i.Maior número;
#ii.Menor número;
#iii.Soma de todos os números gerados;
#iv.Média e desvio padrão.


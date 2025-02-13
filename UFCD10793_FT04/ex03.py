"""Fazer um programa para ler quatro números inteiros e positivos, calcular e devolver a sua média.-
usando o ciclo while"""

contador = 0 
while contador <4:
    numero = int(input(f"Introduza o {contador+1}º número: "))
    soma = soma + numero     
    contador =contador + 1
    
print(contador)
media = soma / contador
print(f"A média dos números introduzidos é {media}")
    
# x+=1 é o mesmo que x = x + 1
# x-=1 é o mesmo que x = x - 1
# x*=1 é o mesmo que x = x * 1
# x/=1 é o mesmo que x = x / 1
# x%=1 é o mesmo que x = x % 1

#opção 2
contador = 1
soma = 0
while contador <=4:
    numero = int(input(f"Introduza o {contador}º número: "))
    soma = soma + numero     
    contador =contador + 1
print(contador)
media = soma / (contador-1)
print(f"A média dos números introduzidos é {media}")

#opção 3
import statistics
contador = 1
lista = []
while contador <=4:
    numero = int(input(f"Introduza o {contador}º número: "))
    lista.append(numero)
    contador =contador + 1
    
media = statistics.mean(lista)
print(lista)
print(f"A média dos números introduzidos é {media}")

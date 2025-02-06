# Solicita três números reais ao utilizador
numero1 = float(input("Por favor, insira o primeiro número real: "))
numero2 = float(input("Por favor, insira o segundo número real: "))
numero3 = float(input("Por favor, insira o terceiro número real: "))

#1 Encontra o maior número entre os três
maior = numero1   #maior é definido como numero1. ponto de partida para fazer a comparação.
#2 o código verifica se numero2 ou numero3 são maiores que o valor atual de maior. Se for o caso, maior é atualizado para o novo valor mais alto. 
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3
# Imprime o maior número
print(f"O maior número é {maior}.")
'''Escreve uma função em Python que, dados a medida do comprimento do lado de
um quadrado imprima os valores do seu perímero e da sua área (area=lado x lado; perimetro = 4 x lado).'''

def calcular_quadrado(lado):
    area = lado * lado
    perimetro = 4 * lado
    print(f"Área: {area}")
    print(f"Perímetro: {perimetro}")

# Exemplo de uso
lado = float(input("Digite o comprimento do lado do quadrado: "))
calcular_quadrado(lado)
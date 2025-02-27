'''Escreve uma função em Python que, dados a medida do comprimento dos três
lados de um triângulo diga se o mesmo é equilátero, isósceles ou escaleno.'''

def tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Equilátero"  # Todos os lados são iguais
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"  # Dois lados são iguais
    else:
        return "Escaleno"  # Todos os lados são diferentes

# Exemplo de uso
l1 = float(input("Digite o primeiro lado: "))
l2 = float(input("Digite o segundo lado: "))
l3 = float(input("Digite o terceiro lado: "))

print("O triângulo é:", tipo_triangulo(l1, l2, l3))
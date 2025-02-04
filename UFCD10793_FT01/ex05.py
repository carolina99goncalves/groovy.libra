print("Programa para calcular o valor da hipotenusa de um triangulo-rectangulo")

import math

adjacente=input("Introduza o comprimento do cateto adjacente:")
adjacente=float(adjacente)
oposto=input("Introduza o comprimento do cateto oposto:")
oposto=float(oposto)

hipotenusa= math.sqrt(adjacente**2 + oposto**2)
print(f"o comprimento da hipotenusa deste triangulo-rectangulo é:{hipotenusa}")
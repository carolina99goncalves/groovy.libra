'''Escreve um programa para classificar um triângulo de acordo com o comprimento dos seus lados. 
Considere as seguintes informações:
• Triângulo equilátero: todos os lados possuem o mesmo comprimento;
• Triângulo escaleno: todos os lados possuem comprimento diferente;
• Triângulo isósceles: caracterizado por ter dois lados com o mesmo comprimento.'''

# Solicita os comprimentos dos três lados do triângulo
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

# Verifica se é um triângulo válido (condição da desigualdade triangular)
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    # Classifica o triângulo
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero.")
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("O triângulo é escaleno.")
    else:
        print("O triângulo é isósceles.")
else:
    print("Os valores inseridos não formam um triângulo.")

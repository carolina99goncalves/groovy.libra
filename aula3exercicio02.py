'''Escreva um programa que solicite ao utilizador dois números inteiros a operação matemática a ser realizada 
(+,-,* e /). Utilize a estrutura match...case para executar a operação escolhida e devolver o resultado.'''

# Solicita os dois números inteiros e a operação matemática a ser realizada
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Utiliza a estrutura match...case para executar a operação
match operacao:
    case "+":
        resultado = numero1 + numero2
        print(f"O resultado de {numero1} + {numero2} é {resultado}")
    case "-":
        resultado = numero1 - numero2
        print(f"O resultado de {numero1} - {numero2} é {resultado}")
    case "*":
        resultado = numero1 * numero2
        print(f"O resultado de {numero1} * {numero2} é {resultado}")
    case "/":
        if numero2 == 0:
            print("Erro: Não é possível dividir por zero!")
        else:
            resultado = numero1 / numero2
            print(f"O resultado de {numero1} / {numero2} é {resultado}")
    case _:
        print("Operação inválida! Escolha uma operação válida (+, -, *, /).")

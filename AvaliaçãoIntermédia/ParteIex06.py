'''Elabora uma script em python que peça ao utilizador dois números e devolva a divisão do 
primeiro número introduzido pelo seguinte. Trate erros como divisão por zero e valores inválidos.'''

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = num1 / num2  # Se num2 for 0, gera ZeroDivisionError
    print(f"O resultado da divisão de {num1} por {num2} é {resultado:.2f}")

except ValueError:
    print("Erro! Certifique-se de inserir números válidos.")

except ZeroDivisionError:
    print("Erro! A divisão por zero não é permitida.")
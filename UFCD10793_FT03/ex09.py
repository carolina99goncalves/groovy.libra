'''O Índice de Massa Corporal (IMC) é utilizado para medir o peso ideal de uma pessoa. 
Escreve um programa que peça o nome, a idade, o peso e a altura do utilizador e que, de seguida, 
calcule e mostre o resultado do seu IMC e classifique esse resultado de acordo com as seguintes condições:
•IMC<17 - Muito abaixo do peso ideal
•17<=IMC<18,5 - Abaixo do peso
•18,5<=IMC<25 - Peso normal
•25<=IMC<30 - Acima do peso
•30<=IMC<35 - Obesidade I
•35<=IMC<40 - Obesidade II (severa)
•IMC>=40 - Obesidade III (mórbida)
Nota: IMC=massa/(altura*altura)'''

# Solicita os dados ao utilizador
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Mostra o IMC calculado
print(f"\n{nome}, seu IMC é: {imc:.2f}")

# Classifica o IMC de acordo com as faixas
if imc < 17:
    classificacao = "Muito abaixo do peso ideal"
elif 17 <= imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    classificacao = "Peso normal"
elif 25 <= imc < 30:
    classificacao = "Acima do peso"
elif 30 <= imc < 35:
    classificacao = "Obesidade I"
elif 35 <= imc < 40:
    classificacao = "Obesidade II (severa)"
else:
    classificacao = "Obesidade III (mórbida)"

# Exibe a classificação do IMC
print(f"Classificação: {classificacao}")


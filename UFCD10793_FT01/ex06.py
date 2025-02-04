print("Vou lhe pedir para inserir uma quantidade de horas\n aquantidade de minutos e segundos\n e vou lhe dizer quantos segundos são.\n")

horas = input("Digite a quantidade de horas: ")

minutos = input("Digite a quantidade de minutos: ")

segundos = input("Digite a quantidade de segundos: ")

horas = int(horas)

minutos = int(minutos)

segundos = int(segundos)

segundos = horas * 3600 + minutos * 60 + segundos

output = f"O total de segundos é: {segundos}"

print(output)
"""Considera a lista idades=[25, 15, 19, 22, 37, 78, 46, 2, 67]"""
#Indique quantas pessoas são menores de idade
#Ordene a lista por ordem decrescente
#Pede ao utilizador uma idade e verifica se essa idade está na lista.
    #- Se estiver faz print("A idade está na lista")
    #- Caso contrário faz o print("não existe ninguém com essa idade na lista")

# Lista de idades
idades = [25, 15, 19, 22, 37, 78, 46, 2, 67]

# Quantas pessoas são menores de idade (idade < 18)
menores = sum(1 for idade in idades if idade < 18)
print(f"Número de pessoas menores de idade: {menores}")

# Ordena a lista por ordem decrescente
idades.sort(reverse=True)
print(f"Lista ordenada por ordem decrescente: {idades}")

# Pede ao utilizador uma idade e verifica se está na lista
idade_solicitada = int(input("Digite uma idade para verificar se está na lista: "))

if idade_solicitada in idades:
    print("A idade está na lista")
else:
    print("Não existe ninguém com essa idade na lista")
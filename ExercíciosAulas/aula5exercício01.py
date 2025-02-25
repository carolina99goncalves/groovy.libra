'''Escreve um programa que, dada uma sequência de numeros inteiros  (todos fornecidos na mesma linha, 
separados por espaços) , imprima a média desses numeros.'''


# Ler a entrada como string
entrada = input("Digite os números inteiros separados por espaço:")

# Remover espaços extra e dividir a string numa lista
numeros_str = entrada.strip().split()

#Verificar se a lista não está vazia
if numeros_str:
    # Somar os números convertidos para inteiro manualmente
    soma = 0
    quantidade = 0 
    
    for num in numeros_str:
        soma += int(num) #Converter a string para inteiro e somar
        quantidade += 1 #Contas quantos números existem
    
    media = soma / quantidade  # Calcular a média
    print(f"Média: {media:.2f}")  # Exibir com duas casas decimais
else:
    print("Nenhum número foi inserido.")
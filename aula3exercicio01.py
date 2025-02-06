'''Escreve um programa que receba o nome de um produto e o seu preço, e retorne o preço total considerando os descontos seguintes:
1.
Se o produto for um smartphone, será aplicado um desconto de 10%.
2.
Se o produto for um tablet, será aplicado um desconto de 15%.
3.
Se o produto for um laptop, será aplicado um desconto de 20%.
4.
Para qualquer outro produto, não haverá desconto.
Utilize a estrutura match...case para determinar o desconto a ser aplicado.'''

# Recebo o nome do produto e o preço
produto = input("Digite o nome do produto: ").lower()  # Para ignorar diferenças de maiúsculas/minúsculas
preco = float(input("Digite o preço do produto: "))

# Aplica o desconto com base no produto usando match...case
match produto:
    case "smartphone":
        desconto = 0.10  # Desconto de 10% para smartphone
    case "tablet":
        desconto = 0.15  # Desconto de 15% para tablet
    case "laptop":
        desconto = 0.20  # Desconto de 20% para laptop
    case _:
        desconto = 0  # Sem desconto para outros produtos
        
# Calcula o preço final com o desconto
preco_final = preco * (1 - desconto)

# Exibe o preço final com o desconto aplicado
if desconto > 0:
    print(f"O produto {produto} tem um desconto de {desconto*100}%.")
else:
    print(f"O produto {produto} não tem desconto.")

print(f"O preço final do {produto} é: E€{preco_final:.2f}") 

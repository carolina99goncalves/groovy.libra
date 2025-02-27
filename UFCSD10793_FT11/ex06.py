'''Escreve uma função que, dado o número do mês retorne o mesmo, por extenso.'''

def mes_por_extenso(numero):
    meses = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }
    return meses.get(numero, "Mês inválido")

# Exemplo de uso
num = int(input("Digite o número do mês (1-12): "))
print("Mês:", mes_por_extenso(num))
"""Considere a seguinte variável que armazena uma string com um conjunto de datas separadas pelo caracter “,”.
datas="12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"
Escreve um programa em Python que
"""

#a.Armazene as diferentes datas numa string
datas = "12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"
lista_datas = datas.split(",")

#b.Imprima as datas correspondentes ao ano de 2022;
datas_2022 = [data for data in lista_datas if "2022" in data]
print("Datas de 2022:", ", ".join(datas_2022))

#c.Crie uma nova lista (dias) e na mesma armazena o dia de cada uma das datas. 
dias = sorted([int(data[:2]) for data in lista_datas])
# Ordene a lista de forma crescente e imprima a mesma.
print("Dias ordenados:", dias)
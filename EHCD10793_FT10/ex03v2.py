#Considere a seguinte variável que armazena uma string com um conjunto de datas separadas pelo caracter ",".
datas = "12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"
#Escreve um programa em Python que:
#a. Armazene as diferentes datas numa string;
data = datas.split(",")
print(data)

#b Imprima as datas correspondentes ao ano de 2022;
for i in data:
    if "2022" in i:
        print(i)
#c Cria uma nova lista (dias) e na mesma armazena o dia de cada uma das datas. Ordene a lista de forma crescente e imprima a mesma.
dias = []
for n in data:
    dias.append(n[:2])
dias.sort()
print(dias)
'''Elabora um programa para escrever no ecrã os números de 1 a 100 e os respetivos quadrados.'''


numero =1 #começa no 1
while numero <=100: # Corre enquanto o numero for menor ou igual a 100
    print(f"{numero} -> {numero**2}") #mostra o número e o quadrado
    numero +=1 #incrementa para o número seguinte
    
#outra resolução
i=1
while i<=100:
    print(f"{i}\t{i**2}")
    i=i+1
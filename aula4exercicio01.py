for i in range(1,11): #outer loop de 1 a 10
    #nested loop (para cada valor de i, j varia de 1 a 10)
    #iterações de 1 to 10
    for j in range(1,11):
        #print multiplication
        multiplicacao = i * j #calcula a multiplicaçao de i por j
        print ("%d*%d=%d\n" % (i,j, multiplicacao)) #imprime o resultado 
        
print("concluido") #indica que o processo foi concluido

#outra resolução

for i in range(1, 11):  # Loop externo (de 1 a 10)
    # Loop interno (para cada valor de i, j varia de 1 a 10)
    for j in range(1, 11):
        multiplicacao = i * j  # Calcula a multiplicação de i por j
        
        
        print(f"{i}*{j}={multiplicacao}\n")
        
        # Imprime o resultado
print("concluido")  # Indica que o processo foi concluído
'''Escrever a tabuada de um número inteiro fornecido pelo utilizador'''
    
    
while True:
    try:
        num = int(input("Digite um número: "))
        break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
    except:
        print("Erro inesperado. Tente novamente.")
    finally:
        print("Fim do programa.")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
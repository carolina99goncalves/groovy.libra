while True:
    try:
        # Pede um número
        numero = int(input("Digite um número inteiro positivo: "))

        # Verifica se o número é positivo
        if numero < 1:
            print("Por favor, insira um número inteiro positivo.")
            continue

        # Calcula a soma dos números de 1 até esse número
        soma = sum(range(1, numero + 1))

        # Resultado
        print(f"A soma dos números de 1 até {numero} é {soma}")
        break  # Sai do loop se tudo correr bem

    except ValueError:
        print("Erro: Insere um número inteiro válido.")
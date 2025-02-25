Txt = """Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte."""

# a) Imprimir o texto em maiúsculas
print("Texto em maiúsculas:")
print(Txt.upper())

# b) Pedir uma palavra ao utilizador e verificar se está no texto
palavra = input("\nDigite uma palavra para procurar no texto: ")
Txt_minusculo = Txt.lower()  # Converter texto para minúsculas
palavra_minuscula = palavra.lower()  # Converter palavra para minúsculas

if palavra_minuscula in Txt_minusculo:
    print("A palavra", palavra, "está no texto.")
else:
    print("A palavra", palavra, "NÃO está no texto.")

# c) Contar quantas vezes a letra "O" aparece no texto
Txt_minusculo = Txt.lower()  # Converter para minúsculas
contagem_o = Txt_minusculo.count('o')  # Contar ocorrências da letra "o"

print("\nA letra 'O' aparece", contagem_o, "vezes no texto.")

# d) Substituir a letra "P" por "_"
Txt_modificado = Txt.replace('P', '_')  # Substituir "P" por "_"
Txt_modificado = Txt_modificado.replace('p', '_')  # Substituir "p" por "_"

print("\nTexto modificado:")
print(Txt_modificado)
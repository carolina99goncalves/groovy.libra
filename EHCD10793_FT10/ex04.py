'''4. Considere a seguinte variável:
Txt="""Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte.'''

# Definição do texto
Txt = """Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte."""

#a.Imprima o texto anterior todo em maiúsculas;
print("Texto em maiúsculas:\n", Txt.upper())

#b.Peça uma palavra ao utilizador e verifique se a mesma está ou não no texto, 
#devolvendo o resultado ao utilizador.
palavra = input("\nDigite uma palavra para procurar no texto: ")
if palavra.lower() in Txt.lower():
    print(f"A palavra '{palavra}' está no texto.")
else:
    print(f"A palavra '{palavra}' NÃO está no texto.")

#c.Imprima o número de vezes que a letra ‘O’ ocorre no texto
contagem_o = Txt.lower().count('o')
print(f"\nA letra 'O' aparece {contagem_o} vezes no texto.")

#d.Substitua todaa as ocorrências da letra ‘P’ no texto por ‘_’
Txt_modificado = Txt.replace('P', '_').replace('p', '_')
print("\nTexto modificado:\n", Txt_modificado)
"""Implemente um programa que, dada uma letra (S, C ou V), indique o estado civil deuma pessoa."""
#input e tudo o resto deve estar ou em maiusculas ou minusculas

estado=str(input("Introduza o seu estado civil: S - Solteiro, C - Casado, D - Divorciado, V - Viúvo\n---->\t"))
match estado:
    case "S":
        print("O estado cívil é: Solteiro(a)")
    case "C":
        print("O estado cívil é: Casado(a)")
    case "D":
        print("O estado cívil é: Divorciado(a)")
    case "V":
        print("O estado cívil é: Viúvo(a)")
    case _:
        print("Estado cívil desconhecido")
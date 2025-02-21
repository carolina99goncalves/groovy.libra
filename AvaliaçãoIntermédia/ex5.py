'''A empresa DataSecure precisa de um sistema que copie ficheiros binários de forma eficiente e segura. 
Para garantir a integridade dos dados, o sistema deve:'''
# a)Solicitar o nome de um ficheiro binário (ex.: imagem, PDF, áudio) que o utilizador deseja copiar.
# b)Criar uma cópia exata desse ficheiro, preservando os dados originais.
# c)Verificar se a cópia foi bem-sucedida, comparando os conteúdos dos dois ficheiros através do cálculo de um hash MD5.
# d)Exibir uma mensagem de sucesso ou erro informando se os ficheiros são idênticos.

import hashlib
import os
def calcular_hash(ficheiro):
    """Calcula o hash MD5 de um ficheiro binário para verificar integridade."""
    hash_md5 = hashlib.md5()
    with open(ficheiro, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""): # Lê o ficheiro em blocos de 4KB
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def copiar_ficheiro_binario(origem, destino):
'''Copia um ficheiro binário e verifica a integridade dos dados.'''
try:
    if not os.path.exists(origem): # Verificar se o ficheiro de origem existe
        print("Erro: O ficheiro de origem não existe.")
        return
# Copiar o ficheiro binário
with open(origem, "rb") as f_origem, open(destino, "wb") as f_destino:
    for chunk in iter(lambda: f_origem.read(4096), b""): # Copia em blocos de 4KB
        f_destino.write(chunk)
# Verificar integridade dos ficheiros
    if calcular_hash(origem) == calcular_hash(destino):
    print(f"Sucesso! O ficheiro '{destino}' foi copiado corretamente.")
    else:
    print("Erro: A cópia do ficheiro não é idêntica ao original.")
except Exception as e:
print(f"Erro inesperado: {e}")
    
# Solicitar entrada do utilizador
ficheiro_origem = input("Digite o nome do ficheiro binário a copiar: ")
ficheiro_destino = "copia_" + ficheiro_origem # Criar nome para o ficheiro copiado

# Executar a cópia e validação
copiar_ficheiro_binario(ficheiro_origem, ficheiro_destino)
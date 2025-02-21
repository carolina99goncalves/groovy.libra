'''A empresa DataSecure precisa de um sistema que copie ficheiros binários de forma eficiente e segura. 
Para garantir a integridade dos dados, o sistema deve:'''
# a)Solicitar o nome de um ficheiro binário (ex.: imagem, PDF, áudio) que o utilizador deseja copiar.

import hashlib
import os
def calcular_hash(ficheiro):
    """Calcula o hash MD5 de um ficheiro binário para verificar integridade."""
    hash_md5 = hashlib.md5()
    with open(ficheiro, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""): # Lê o ficheiro em blocos de 4KB
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# b)Criar uma cópia exata desse ficheiro, preservando os dados originais.


# c)Verificar se a cópia foi bem-sucedida, comparando os conteúdos dos dois ficheiros através do cálculo de um hash MD5.
#d)Exibir uma mensagem de sucesso ou erro informando se os ficheiros são idênticos.
#https://docs.python.org/3/library/sqlite3.html

import sqlite3  # Biblioteca SQLite

# Base de dados (criar se não existir)
conexao = sqlite3.connect("empresa.db")

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar a tabela funcionários
cursor.execute("""
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        salario REAL NOT NULL
    )
""")

# Guardar mudanças e fechar conexão
conexao.commit()
conexao.close()

# Reabrir a conexão 
conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

# Inserir alunos na tabela"
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", ("Carolina Goncalves", "Gestora", 3500))
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", ("Maria Joana", "Programadora", 4000))
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", ("Saif Ferreira", "Designer", 2000))
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", ("João Silva", "Cabeleireira", 4500))  # Novo funcionário
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", ("Ana Pereira", "Engenheira", 5000))  # Novo funcionário


# Guardar mudanças e fechar conexão
conexao.commit()
conexao.close()


#Consultar dados
conexao = sqlite3.connect("empresa.db") #abrir a base de dados empresa
cursor = conexao.cursor() #O cursor ajuda a ver dentro da base de dados

# Consultar todos os funcionários
cursor.execute("SELECT * FROM funcionarios") #Pedimos ao cursor a lista de todos os funcionários
funcionarios = cursor.fetchall() #Guardamos a lista de funcionários 

# Exibir os resultados
print("Lista de Funcionarios:") #Dizemos que vamos mostrar a lista de funcionários
for funcionario in funcionarios: #Mostramos cada funcionário um por um
    print(funcionario)

conexao.close() #Fechamos a base de dados

#Atualizar dados

conexao = sqlite3.connect("empresa.db")
cursor=conexao.cursor()

#Atualizar o salario de Maria Joana
cursor.execute("UPDATE funcionarios SET salario = 6000 where nome='Maria Joana'")

#modifica o codigo para aumentr o salario de todos os funcionarios em 5%
conexao.commit()
conexao.close()

conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

cursor.execute("UPDATE funcionarios SET salario = salario * 1.05") # Atualizar todos os salários em 5%

conexao.commit()

cursor.execute("SELECT * FROM funcionarios") # Verificar os novos salários
print("OK. Salários atualizados:")
for funcionario in cursor.fetchall():
    print(funcionario)

conexao.close()


conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

# Eliminar um funcionário específico
cursor.execute("DELETE FROM funcionarios WHERE nome = 'Carolina Goncalves'")

cursor.execute("SELECT * FROM funcionarios")
print("\nLista de Funcionários Atualizada:")
for funcionario in cursor.fetchall():
    print(funcionario)

conexao.close()

#Modifica o código para eliminar todos os funcionários com um salário inferior a 3000


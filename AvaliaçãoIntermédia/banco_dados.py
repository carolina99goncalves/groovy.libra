#https://docs.python.org/3/library/sqlite3.html

import sqlite3  # Biblioteca SQLite

# 1. Base de dados (criar se não existir)
conexao = sqlite3.connect("empresa.db")

# 1. Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# 1. Criar a tabela funcionários
cursor.execute("""
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        salario REAL NOT NULL
    )
""")

# 1. Guardar mudanças e fechar conexão
conexao.commit()
conexao.close()

# 2. Reabrir a conexão 
conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

# 2. Inserir alunos na tabela"
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", ("Carolina Goncalves", "Gestora", 3500))
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", ("Maria Joana", "Programadora", 4000))
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", ("Saif Ferreira", "Designer", 2000))
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", ("João Silva", "Cabeleireira", 4500))  # Novo funcionário
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", ("Ana Pereira", "Engenheira", 5000))  # Novo funcionário


# 2. Guardar mudanças e fechar conexão
conexao.commit()
conexao.close()


# 3. Consultar dados
conexao = sqlite3.connect("empresa.db") #abrir a base de dados empresa
cursor = conexao.cursor() #O cursor ajuda a ver dentro da base de dados

# 3. Consultar todos os funcionários
cursor.execute("SELECT * FROM funcionarios") #Pedimos ao cursor a lista de todos os funcionários
funcionarios = cursor.fetchall() #Guardamos a lista de funcionários 

# 3. Exibir os resultados
print("Lista de Funcionarios:") #Dizemos que vamos mostrar a lista de funcionários
for funcionario in funcionarios: #Mostramos cada funcionário um por um
    print(funcionario)

conexao.close() #Fechamos a base de dados

# 4. Atualizar dados

conexao = sqlite3.connect("empresa.db")
cursor=conexao.cursor()

# 4. Atualizar o salario de Maria Joana
cursor.execute("UPDATE funcionarios SET salario = 6000 where nome='Maria Joana'")

# 4. modifica o codigo para aumentr o salario de todos os funcionarios em 5%
conexao.commit()
conexao.close()

conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

# 4. Atualizar todos os salários em 5%
cursor.execute("UPDATE funcionarios SET salario = salario * 1.05") 

conexao.commit()

# 4. Verificar os novos salários
cursor.execute("SELECT * FROM funcionarios") 
print("OK. Salários atualizados:")
for funcionario in cursor.fetchall():
    print(funcionario)

conexao.close()


conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

# 5. Eliminar um funcionário específico
cursor.execute("DELETE FROM funcionarios WHERE nome = 'Carolina Goncalves'")

cursor.execute("SELECT * FROM funcionarios")
print("\nLista de Funcionários Atualizada:")
for funcionario in cursor.fetchall():
    print(funcionario)

conexao.close()

# 5. Modifica o código para eliminar todos os funcionários com um salário inferior a 3000
conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

# 5. Eliminar todos os funcionários com salário inferior a 3000
cursor.execute("DELETE FROM funcionarios WHERE salario < 3000")

conexao.commit()

# 5. Mostrar a lista atualizada de funcionários
cursor.execute("SELECT * FROM funcionarios")
print("\nLista de Funcionários após remoção dos salários menores que 3000:")
for funcionario in cursor.fetchall():
    print(funcionario)

conexao.close()

conexao = sqlite3.connect("empresa.db")
cursor = conexao.cursor()

def menu():
    while True:
        print("\nMENU DE GESTÃO DE FUNCIONÁRIOS")
        print("1.Adicionar funcionário")
        print("2.Listar funcionários")
        print("3.Atualizar salário")
        print("4.Eliminar funcionário")
        print("5.Sair")
        opcao = input("Escolha uma opção:")
        
        if opcao == '1':
            nome = input("Nome:")
            cargo = input("Cargo:")
            salario = float(input("Salário:"))
            cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", ("Sofia Maria", "Dancarina", 1700))
        elif opcao == '2':
            cursor.execute("SELECT * FROM funcionarios")
            for funcionario in cursor.fetchall():
                print(funcionario)
                
        elif opcao == '3':
            nome = input("Nome do funcionário:")
            novo_salario = float(input("Novo salário:"))
            cursor.execute("UPDATE funcionarios SET salario = ? WHERE nome = ?", (novo_salario, nome))

        
        elif opcao == '4':
            nome = input("Nome do funcionário a eliminar:")
            cursor.execute("DELETE FROM funcionarios WHERE nome = ?", (nome,))
        
        elif opcao == '5':
            conexao.commit()
            conexao.close()
            break
        else: 
            print("Opção inválida! Tente novamente.")
            
#Criar conexão
conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()
menu()
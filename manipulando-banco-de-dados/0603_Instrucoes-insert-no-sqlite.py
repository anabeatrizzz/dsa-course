import sqlite3

# Criando uma conexao.
conexao = sqlite3.connect("exemplo.db")

# Criando um cursor.
cursorr = conexao.cursor()

# Criando funcao que cria uma tabela
def criar():
    cursorr.execute("CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, nome TEXT, valor REAL)")

# Criando uma funcao que insere dados na tabela.
def inserir():
    cursorr.execute("10, 10-10-2010, Melancia, 10.00")
    conexao.commit()
    cursorr.close()
    conexao.close()

criar()
inserir()
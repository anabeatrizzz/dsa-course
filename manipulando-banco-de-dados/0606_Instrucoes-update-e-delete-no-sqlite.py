import sqlite3
import random
import time
import datetime

# Criando uma conexao.
conexao = sqlite3.connect("exemplo.db")

# Criando um cursor.
cursorr = conexao.cursor()

# Criando funcao que cria uma tabela
def criar():
    cursorr.execute("CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, nome TEXT, valor REAL)")


# Criando uma funcao que insere dados na tabela.
def inserir():
    cursorr.execute("10, 10-10-2010, Melancia, 10.00")
    conexao.commit()
    cursorr.close()
    conexao.close()


# Criando funcao que insere dados na tabela usando variaveis.
def inserir_var():
    nova_data = datetime.datetime.now()
    # Variavel que recebe o horario exato.
    novo_nome = "Abobora"
    # Variavel que recebe um texto.
    novo_valor = random.randrange(50, 100)
    # Variavel que recebe valores entre 50 e 100.
    cursorr.execute("INSERT INTO produtos (date, nome, valor) VALUES (?, ?, ?)", (nova_data, novo_nome, novo_valor))
    # Executando a instrucao sql passando as tres variaveis a cima como parametro.
    conexao.commit()
    # Enviando a instrucao.


def lerTudo():
    cursorr.execute("SELECT * FROM produtos")
    for c in cursorr.fetchall():
        print(c)


def lerAlguns():
    cursorr.execute("SELECT * FROM produtos WHERE valor > 70.00")
    for c in cursorr.fetchall():
        print(c)


def lerColunas():
    cursorr.execute("SELECT * FROM produtos")
    for c in cursorr.fetchall():
        print(c[3])


def atualizar():
    cursorr.execute("UPDATE produtos SET valor = 10.00 WHERE valor = 40.00")
    conexao.commit()
    # O commit faz a gravacao da transacao. Quando executamos comandos como INSERT, UPDATE e DELETE, fazemos uma transacao e devemos usar o commit para gravar o resultado no banco de dados.


def remover():
    cursorr.execute("DELETE FROM produtos WHERE valor = 20.00")
    conexao.commit()


atualizar()
lerTudo()
remover()
lerTudo()
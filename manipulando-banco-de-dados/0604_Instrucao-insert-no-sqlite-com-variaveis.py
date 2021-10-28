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
    cursorr.execute("CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, nome TEXT, valor REAL)")

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

# Faça 10 vezes:
for c in range(10):
    # Chame a funcao.
    inserir_var()
    # Espere um segundo.
    time.sleep(1)
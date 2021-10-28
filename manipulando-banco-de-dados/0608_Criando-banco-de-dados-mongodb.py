# Instalar MongoDB
# Executar o comando pip install pymongo

from pymongo import MongoClient
# funcao MongoClient permite a conexao com o MongoDB

conexao = MongoClient("localhost", 12345)
# MongoClient('onde está o banco de dados', numero da porta)

bd = conexao.cadastrobd
# Criando um banco de dados chamado cadastrobd 

colecao = bd.cadastrobd
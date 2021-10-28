# Instalar MongoDB
# Executar o comando pip install pymongo

from pymongo import MongoClient
# funcao MongoClient permite a conexao com o MongoDB

conexao = MongoClient("localhost", 12345)
# MongoClient('onde está o banco de dados', numero da porta)

bd = conexao.cadastrobd
# Criando um banco de dados chamado cadastrobd 

colecao = bd.cadastrobd

import datetime

documento1 = {"codigo":"12345",
"produto":"geladeira",
"marcas":["brastemp", "consul", "eletrolux"],
"data":datetime.datetime.utcnow()}

colecao = bd.posts

documento_id = colecao.insert_one(documento1)
# Quando um documento é inserido, um id é adicionado automaticamente, se o documento ainda nao conter um.

documento2 = {"codigo":"67890",
"produto":"televisor",
"marcas":["samsung", "parasonic", "lg"],
"data":datetime.datetime.utcnow()}

colecao = bd.posts

documento_id = colecao.insert_one(documento2)

for c in colecao.find():
    print(c)
# Retorna cada chave e valor

bd.name
# Nome do banco de dados
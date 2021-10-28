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

import pymongo

# Quando não se é passado nenhum parametro para o MongoClient, o MondoDB usa o localhost padrão.
conexao = pymongo.MongoClient()

# Listando banco de dados disponiveis.
conexao.database_names()

# Nos permite fazer a conexao especificamente com o banco de dados cadastrobd
bd = conexao.cadastrobd

# Listando as colecoes (tabelas) disponiveis
bd.collection_names()

# Criando uma colecao (tabela)
bd.create_collection("minha_colecao")

bd.collection_names

# Inserindo um documento na colecao criada
bd.minha_colecao.insert_one({
   'titulo': 'MongoDB com Python', 
   'descricao': 'MongoDB é um Banco de Dados NoSQL',
   'by': 'Data Science Academy',
   'url': 'http://www.datascienceacademy.com.br',
   'tags': ['mongodb', 'database', 'NoSQL'],
   'likes': 100
})

bd.minha_colecao.find_one()

# Preparando um documento:
documento3 = {
  "Nome": "Ana",
  "Sobrenome": "Augusto",
  "Twitter": "inexistente"
}

# Inserindo um documento:
bd.minha_colecao.insert_one(documento3)

documento4 = {
  "Site": "http://www.datascienceacademy.com.br",
  "facebook": "facebook.com/dsacademybr"
}

bd.minha_colecao.insert_one(documento4)

# Mostrando documentos dentro da colecao:
for c in bd.minha_colecao.find():
  print(c)

# Conectando a uma colecao:
conectando = bd["minha_colecao"]

# Contando quantos documentos há na colecao:
conectando.count()

buscando = conectando.find_one()
print(buscando)
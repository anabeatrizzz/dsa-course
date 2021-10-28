dicionario = {
  'nome':'Ana',
  'idade': 17,
  'brasileira': True
}

for c, v in dicionario.items():
  print(c, v)
  
import json
json.dumps(dicionario)
with open("dados.json", "w") as arquivo:
  arquivo.write(json.dumps(dicionario))
  
with open("dados.json", "r") as arquivo:
  texto = arquivo.read()
  dados = json.loads(texto)
print(dados)
print(dados["nome"])


from urllib.request import urlopen
resposta = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode("utf8")
dados = json.loads(resposta)[0]
print("Titulo: ", dados["title"])
print("URL: ", dados["url"])
print("Duracao: ", dados["duration"])
print("Numero de visualizacoes: ", dados["stats_number_of_plays"])

import os
primeiro = "dados.json"
segundo = "dados_json.txt"
with open(primeiro, "r") as primeiroo:
    texto = primeiroo.read()
    with open(segundo, "w") as segundoo:
        segundoo.write(texto)

with open("dados_json.txt") as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)
print(dados)
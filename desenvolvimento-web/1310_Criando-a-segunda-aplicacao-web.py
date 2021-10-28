# Importando
from flask import Flask

# Criando a app web
app = Flask(__name__)

# Criando a rota raiz
@app.route("/")
# Se acessarmos essa rota, o texto "Indice!" será mostrado
def indice():
	return "Indice!"

# Criando a rota /ola
@app.route("/ola")
# Quando acessarmos essa rota, o texto "Olá mundo!" será mostrado
def ola():
	return "Olá mundo!"

# Criando a rota /membros
@app.route("/membros")
# Quando acessarmos essa rota, o texto "Membros" será mostrado
def membros():
	return "Membros"

# Criando a rota /membros/alguma_string
@app.route("/membros/<string:nome>/")
# Quando acessarmos essa rota, alguma_string será mostrada
def getMembro(nome):
	return nome

# A app sendo executada no host a na porta do replit
app.run(host='0.0.0.0', port=8080)
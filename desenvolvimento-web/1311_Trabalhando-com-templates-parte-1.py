# Importando
from flask import Flask, flash, redirect, render_template, request, session, abort

# Criando a app web
app = Flask(__name__)

# Criando rota raiz
@app.route("/")
# Quando for acessada, Flask App! será mostrado na tela
def indice():
	return "Flask App!"

# Criando rota /ola/alguma_string
@app.route("/ola/<string:nome>/")
# Quando dor acessada, vai ser carregado um tema para a pagina e vai ser mostrado o texto Hello alguma_string
# OBS: template1.html precisa estar em uma pasta nomeada templates
def ola(nome):
	return render_template('template1.html', nome=nome)

# Aplicativo sendo executado na url http://0.0.0.0:8080/
app.run(host='0.0.0.0', port=8080)

# No arquivo template1.html
# <h1>Hello {{nome}}</h1>
# Arquivo hello4.py
# Importando
from flask import Flask, flash, redirect, render_template, request, session, abort

# Criando a app web
app = Flask(__name__)

# Criando a rota raiz
@app.route("/")
# Quando for acessada, Flask App! será mostrado na tela
def indice():
	return "Flask App!"

# Criando a rota /ola/alguma_string
@app.route("/ola/<string:nome>/")
# Quando for acessada, o tema template2.html será carregado e o que estiver neste arquivo será executado
# OBS: template1.html e layout.html precisam estar em uma pasta nomeada templates
def ola(nome):
	return render_template('template2.html',nome=nome)

# Aplicativo sendo executado na url http://0.0.0.0:8080/
app.run(host='0.0.0.0', port=8080)

# No arquivo layout.html
"""
<html>
<head>
    <title>Website</title>
<style>
@import url(http://fonts.googleapis.com/css?family=Amatic+SC:700);

body{
    text-align: center;
}
h1{
    font-family: 'Amatic SC', cursive;
    font-weight: normal;
    color: #8ac640;
    font-size: 2.5em;
}

img{
	width: 50%;
}

</style>

</head>
<body>
 {% block body %}{% endblock %}

</body>
</html>
"""

# No arquivo template2.html
"""
{% extends "layout.html" %}
{% block body %}

<div class="block1">
<h1>Hello {{nome}}!</h1>
  <h2>Pronto para aprender algo novo hoje? Um dia sem aprender algo novo é um dia perdido!</h2>
  <p>"O único limite que existe é aquele que você impõe a si mesmo."</p>
<img src="https://images.freeimages.com/images/large-previews/007/books-1419617.jpg">
</div>
{% endblock %}
"""
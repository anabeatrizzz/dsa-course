# Importando
from flask import Flask

# Criando a app web
app = Flask(__name__)

# Criando rota raiz
@app.route("/")

# Indicando o que o app fará, irá mostrar "Olá mundo!" na tela
def hello():
	return "Olá mundo!"

# Executando a app web no host e na porta do replit
app.run(host='0.0.0.0', port=8080)
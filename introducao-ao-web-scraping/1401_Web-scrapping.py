# Shared via Compiler App https://g633x.app.goo.gl/TPlw
# Importando módulo que lida com links
import urllib.request

# Importando biblioteca para deixar o HTML mais legível
from bs4 import BeautifulSoup

# Com o site do python aberto como url:
with urllib.request.urlopen("https://www.python.org") as url:
	# Leia o html da página e guarde em pagina
	pagina = url.read()

# Mostre o HTML da página
print(pagina)

# A função BeautifulSoup() nos ajuda na análise da de uma página html
# O html.parser é para especificar que ocorrerá uma análise em um html
analise = BeautifulSoup(pagina, "html.parser")

# Mostrando a primeira tag title de pagina
print(analise.title)

# Mostrando a primeira tag title de pagina como uma string
print(analise.title.string)

# Mostrando a primeira tag a em pagina
print(analise.a)

# Mostrando todas as tag a em pagina
print(analise.find_all("a"))

# Guardando a primeira tag table em pagina
tabelas = analise.find("table")

# Mostrando a primeira tag table
print(tabelas)
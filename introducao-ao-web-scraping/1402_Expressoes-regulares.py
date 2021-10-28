# Shared via Compiler App https://g633x.app.goo.gl/TPlw
# Pacote que lida com expressões regulares
import re

lista_palavras = ["Ana", "Justin", "Lilica"]

texto = "Eu gosto mais da Lilica do que do Justin."

for c in lista_palavras:
	print(f'Buscando por {c} em {texto}')
	if re.search(c, texto):
		print("Palavra encontrada")
	else:
		print("Palavra não encontrada")

# -----

divisorio = "@"

frase = 'Qual o domínio de alguém com o e-mail: aluno@gmail.com'

print(re.split(divisorio, frase))

# -----

def encontra_padrao(lista, frase):
	for item in lista:
		print(f'Pesquisando na frase: {item}')
   print(re.findall(item, frase))
   print('\n')

frase_padrao = 'zLzL..zzzLLL...zLLLzLLL...LzLz...dzzzzz...zLLLL'

lista_padroes = [ 'zL*', 'zL+', 'zL?', 'zL{3}', 'zL{2,3}']

# [0] --> z seguido de 0 ou mais L
# [1] --> z seguido por 1 ou mais L
# [2] --> z seguido por 0 ou 1 L
# [3] --> z seguido por 3 L
# [4] --> z seguido por 2 a 3 L

encontra_padrao(lista_padroes, frase_padrao)

# -----
frase = 'Esta é uma string com pontuação. Isso pode ser um problema quando fazemos mineração de dados em busca de padrões! Não seria melhor retirar os sinais ao fim de cada frase?'

# Mostrando apenas as palavras da string em frase
print(re.findall('[^!.? ]+', frase))

# -----

frase = 'Esta é uma frase de exemplo. Vamos verificar quais padrões serão encontrados.'

lista_padroes = [ '[a-z]+', '[A-Z]+', '[a-zA-Z]+', '[A-Z][a-z]+']

# [0] --> sequência de letras minúsculas
# [1] --> sequência de letras maiúsculas
# [2] --> sequência de letras minúsculas e maiúsculas
# [3] --> uma letra maiúscula, seguida de uma letra minúscula

# -----
frase = "Esta é uma string com alguns números, como 1287 e um símbolo @"

lista_padroes = [ r'\d+', r'\D+', r'\s+', r'\S+', r'\w+', r'\W+']

# [0] --> sequência de dígitos
# [1] --> sequência de não-dígitos
# [2] --> sequência de espaços
# [3] --> sequência de não-espaços
# [4] --> caracteres alfanuméricos
# [5] --> não-alfanumérico

encontra_padrao(lista_padroes, frase)
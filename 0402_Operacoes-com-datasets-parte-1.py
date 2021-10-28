# Fonte: Data Science Academy

# Automatizando o processo de gravação:
arquivo3 = input("Digite um nome para o arquivo: ")
arquivo3 += ".txt"
# É incluído a extensão .txt no nome do arquivo.
arquivo4 = open(arquivo3, "w")
# Abrindo o novo arquivo criado para escrita.
arquivo4.write("Incluindo texto")
# Escrevendo 'Incluindo texto' no arquivo.
arquivo4.close()
# Fechando o arquivo.
arquivo4 = open(arquivo3, "r")
# Abrindo o arquivo para leitura.
print(arquivo4.read())
# Mostrando o conteúdo que há no arquivo
arquivo4.close()
# Fechando o arquivo

# Dividindo o arquivo em linhas:
abrir = open("salarios.csv", "r")
# Abrindo um arquivo para leitura.
dados = abrir.read()
# Lendo o arquivo.
linhas = dados.slipt("\n")
# Separando o arquivo em partes, quando for encontrado um enter.
print(linhas)
# Mostrando essa separação.

# Dividindo o arquivo em colunas:
abrir = open("salarios.csv", "r")
# Abrindo um arquivo para leitura.
dados = abrir.read()
# Lendo o arquivo.
linhas = dados.split("\n")
# Separando o arquivo quando um enter for encontrado.
dados2 = []
# Uma lista vazia.
for c in linhas: # Para cada caracter no arquivo separado:
    linhas2 = c.split(",")
    # Separe quando encontrar uma virgula
    dados2.append(linhas2)
    # Coloque essa separação dentro da lista vazia.
print(dados2)
# Mostre a lista vazia.

# Contando as linhas de um arquivo:
abrir = open("salarios.csv", "r")
# Abrindo um arquivo para leitura.
dados = abrir.read()
# Lendo o arquivo.
linhas = dados.split("\n")
# Separando o arquivo quando um enter for encontrado.
dados2 = []
# Uma lista vazia.
for c in linhas: # Para cada caracter no arquivo separado:
    linhas2 = c.split(",")
    # Separe quando encontrar uma virgula
    dados2.append(linhas2)
    # Coloque essa separação dentro da lista vazia.
cont = 0 # Contador que inicia em 0
for c in dados2: # Para cada coisa dentro de dados2:
    cont += 1 # Cont recebe +1
print(cont)
# Mostre o numero dentro de cont

# Contando o número de colunas de um arquivo:
abrir = open("salarios.csv", "r")
# Abrindo um arquivo para leitura.
dados = abrir.read()
# Lendo o arquivo.
linhas = dados.split("\n")
# Separando o arquivo quando um enter for encontrado.
dados2 = []
# Uma lista vazia.
for c in linhas: # Para cada caracter no arquivo separado:
    linhas2 = c.split(",")
    # Separe quando encontrar uma virgula
    dados2.append(linhas2)
    # Coloque essa separação dentro da lista vazia.
    umLinha = dados2[0] # Quantas colunas há em uma linha?
cont = 0 # Contador que inicia em 0
for c in umLinha: # Para cada coisa dentro de umLinha:
    cont += 1 # Cont recebe +1
print(cont) # Mostre o numero final dentro de cont
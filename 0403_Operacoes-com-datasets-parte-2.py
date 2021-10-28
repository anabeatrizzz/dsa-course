# Importando um arquivo que contem dados com pandas:

import pandas
# Importando biblioteca pandas.
arquivo = "binary.csv"
# Colocando um arquivo .csv numa variável.
ler = pandas.read_csv(arquivo)
# A função read_csv da biblioteca pandas irá ler o arquivo.
ler.head()
# Essa linha retorna as primeiras 4 linhas do arquivo.
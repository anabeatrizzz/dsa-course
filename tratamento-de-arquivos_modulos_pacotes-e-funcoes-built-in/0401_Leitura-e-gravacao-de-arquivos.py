# Fontes: W3Schools e Data Science Academy

# Por exemplo, temos um arquivo .txt chamado teste1 e nele está escrito 'Python é uma linguagem poderosa'
arquivo = open("arquivos/teste1.txt", "r") # Abra o arquivo teste1 apenas para leitura
# OU
# arquivo = open("teste1.txt", "r")
print(arquivo.read())
# Resultado: 'Python é uma linguagem poderosa'

print(arquivo.tell())
# Resultado: O numero de caracteres que o arquivo teste1 possui

print(arquivo.seek(0, 0))
# Retornamos ao inicio do arquivo pois, definimos linha 0 e coluna 0
# Resultado: 0

print(arquivo.read(10))
# Resultado: 'Python é u'
# Como estamos no inicio do arquivo será retornado o texto que começa no índice 0 e vai até o índice 9 pois, os espaços também contam como caracteres

arquivo2 = open("teste1.txt", "w")
# Abrindo o arquivo teste1 para escrita
arquivo2.write("Legal")
# Escrevendo 'Legal' dentro do arquivo (subscrevendo o texto antigo)
arquivo2.close()
# Fechando o arquivo

# Se fizessemos os mesmos processos das linhas 4 e 7 de novo, o resultado seria: 'Legal'

arquivo2 = open("teste1.txt", "a")
# Abrindo o arquivo teste1 para acrescentar conteudo
arquivo2.write(" Bacalhau")
# Acrescentando o texto ' Bacalhau' ao arquivo
arquivo2.close()
# Fechando o arquivo

# Se fizessemos os mesmos processos das linhas 4 e 7 de novo, o resultado seria: 'Legal Bacalhau'
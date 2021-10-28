import pandas as pd
import numpy as np

# Criando um dicionario
dados = {
  "Pais":["Brasil", "Peru", "Argentina"],
  "Sigla":["BR", "PER", "ARG"],
  "Populacao":[100, 200, 300]
}

# Criando um dataframe nomeando colunas e índices.
frame2 = pd.DataFrame(dados, columns=["Pais", "Sigla", "Colunas"], index=["um", "dois", "tres"])

# Preenchendo a coluna Colunas com valores de 0 até 3 e mostrando o dataframe frame2.
frame2["Colunas"] = np.arange(4.)
print(frame2)

# Mostrando quantidade, média, valor maximo, valor mínimo e outras características do dataframe frame2.
print(frame2.describe())

# Mostre do índice de nome "um" até o indice de nome "tres".
print(frame2["um":"tres"])

# Há algum valor maior que 100 no dataframe frame2?
print(frame2 > 100)

# Mostrando valores do indice nomeado "tres".
print(frame2.loc["tres"])

# Mostrando valores que estao na linha 2
print(frame2.iloc(2))

# Criando outro dicionário
dados2 = {
    "Dias":[1, 2, 3, 4, 5, 6, 7]
    "Visitantes":[10, 20, 30, 40, 50, 60, 70]
    "Taxas":[80, 90, 100, 110, 120, 130, 140]
}

# Definindo o outro dicionário criado como um dataframe e mostrando-o
frame3 = pd.DataFrame(dados2)
print(frame3)

# Mostrando como o dataframe ficaria se o indice fosse a coluna nomeada "Dias"
print(frame3.set_index("Dias"))

# Mostrando os primeiros valores do dataframe
print(frame3.head())

# Mostrando valores da coluna nomeada "Visitantes"
print(frame3["Visitantes"])

# Mostrando valores das colunas "Visitantes" e "Taxas"
print(frame3[["Visitantes", "Taxas"]])
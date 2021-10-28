import pandas as pd

print("\033[33mUm dataframe é algo semelhante a uma planilha excel.\033[m")
# Criando um dicionario
dados = {
  "Pais":["Brasil", "Peru", "Argentina"],
  "Sigla":["BR", "PER", "ARG"],
  "Populacao":[100, 200, 300]
  }

# Passando o dicionario criado como parametro para o metodo DataFrame do pacote pd
frame = pd.DataFrame(dados)
print(frame)

print("\n")

# Podemos definir nomes para colunas e indices usando as palavras columns e index
# Não existe a coluna Colunas em dados, por isso os valores NaN
frame2 = pd.DataFrame(dados, columns=["Pais", "Sigla", "Colunas"], index=["um", "dois", "tres"])
print(frame2)

print("\n\033[33mMostrando dados da coluna Sigla:\033[m")
print(frame2["Sigla"])

print("\n\033[33mMostrando indices, colunas, valores e tipo de dado:\033[m")
print(frame2.index, "\n")
print(frame2.columns, "\n")
print(frame2.values, "\n")
print(frame2.dtypes)

print("\n\033[33mMostrando dados da linhas de indices 0 e 1:\033[m")
print(frame2[:2])
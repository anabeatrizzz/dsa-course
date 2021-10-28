import pandas as pd
import sys
import numpy as np

frame4 = pd.read_csv("arquivo.csv")
# Se o separador do arquivo não for vírgula, podemos especificar usando sep = "separador"
# Exemplo: frame4 = pd.read_csv("arquivo.csv", sep = "|")

frame4 = pd.read_table("arquivo.csv", sep = ",")

print(frame4)

frame4 = pd.read_csv("salarios.csv", names = ["a", "b", "c", "d"])

dados = pd.read_csv("arquivo.csv")

dados.to_csv(sys.stdout, sep = "|")

datas = pd.date_range("20190101", periods = 10)

frame4 = pd.DataFrame(np.random.randn(10, 4), index = datas, columns = list("ABCD"))
print(frame4)

print(frame4.head())

print(frame4.describe())

# Calculando média das colunas.
print(frame4.mean())

# Calculando média das linhas.
print(frame4.mean(1))

frame4.apply(np.cumsum)

esquerda = pd.DataFrame({
    "chave":["chave1", "chave2"],
    "coluna1":[1, 2]
})

direita = pd.DataFrame({
    "chave":["chave1", "chave2"],
    "coluna2":[3, 4]
})

print(pd.merge(esquerda, direita, on="chave"))

frame4 = pd.DataFrame(np.random.randn(8, 4), columns=["A", "B", "C", "D"])
print(frame4)

l = frame4.iloc[3]

print(frame4.append(l, ignore_index=True))
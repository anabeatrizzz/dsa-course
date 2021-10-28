import pandas as pd
import numpy as np

# Gerando 10 datas e apenas mudando o numero de segundos entre elas.
rng = pd.date_range("1/1/2019", periods=10, freq="S")

# Criando uma serie temporal que usa as datas de rng como indice e numeros de 0 a 20 como valores.
# A série temporal é um dataframe que contém apenas uma coluna de dados.
ts = pd.Series(np.random.randint(0, 20, len(rng)), index=rng)

print(ts)

# Gerando 10 datas apenas mudando os meses entre elas.
rng2 = pd.data_range("1/1/2018", periods=10, freq="M")

ts2 = pd.Series(np.random.randn(len(rng2)), index=rng2)

print(ts2)

import matplotlib.pyplot as plt
from matplotlib import style

# Criando uma serie com valores representando 20 numeros aleatorios, o indice será datas.
ts3 = pd.Series(np.random.randn(20), index=pd.date_range("1/1/2017"), periods=20)

# Fazendo a soma acumulada.
ts3 = ts3.cumsum()

# Mostrando grafico.
print(ts3.plot())

df = pd.DataFrame(np.random.randn(100, 4), index = ts3.index, columns=["A", "B", "C", "D"])
df = df.cumsum()
plt.figure; df.plot; plt.legend(loc="best")

import os

df.to_excel("teste.xlsx", sheet_name="Planilha1")

df2 = pd.read_excel("teste.xlsx", "Planilha1", index_col=None, na_values=["NA"])

print(df2.head())
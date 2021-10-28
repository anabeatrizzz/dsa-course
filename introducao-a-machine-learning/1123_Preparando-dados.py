# Importando módulos
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Guardando o conjunto de dados
df = pd.read_csv("pima-data.csv")

# Mostrando quantas linhas e colunas df possui
print(df.shape)

# Mostrando as 5 primeiras linhas
print(df.head(5))

# Mostrando as 5 últimas linhas
print(df.tail(5))

# Verificando se há valores nulos
print(df.isnull().values.any())

# Quando chamarmos essa função, ela irá mostrar um gráfico indicando a correlação entre as variáveis (colunas)
def plot_corr(df, size=10):
	# A função corr() calcula a correlação usando pares de colunas, excluindo valores NA/nulos.
	corr = df.corr()
	fig, ax = plt.subplots(figsize = (size, size))
	# matshow() mostra uma array como uma matriz no gráfico
	ax.matshow(corr)

	plt.xticks(range(len(corr.columns)), corr.columns)

	plt.yticks(range(len(corr.columns)), corr.columns)

# Mostrando o grafico
plot_corr(df)

# Visualizando a correlação em tabela
# Coeficiente de correlação:
# +1 = forte correlação positiva
# 0 = não há correlação
# -1 = forte correlação negativa
df.corr()

# Substituindo valores da coluna diabetes
diabetes_map = {True : 1, False : 0}

df['diabetes'] = df['diabetes'].map(diabetes_map)

# Verificando como os dados estão distribuídos
num_true = len(df.loc[df['diabetes'] == True])
num_false = len(df.loc[df['diabetes'] == False])
print("Número de Casos Verdadeiros: {0} ({1:2.2f}%)".format(num_true, (num_true/ (num_true + num_false)) * 100))
print("Número de Casos Falsos     : {0} ({1:2.2f}%)".format(num_false, (num_false/ (num_true + num_false)) * 100))
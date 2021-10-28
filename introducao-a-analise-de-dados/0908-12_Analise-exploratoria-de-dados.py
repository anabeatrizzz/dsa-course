import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import colorsys
plt.style.use('seaborn-talk')
import warnings
warnings.filterwarnings("ignore")

# Carregando um arquivo csv usando a função read_csv do pandas.
df = pd.read_csv("../input/2016-new-coder-survey-/2016-FCC-New-Coders-Survey-Data.csv", sep = ',')

# Mostrando apenas algumas linhas do arquivo carregado
print(df.head())

# Fazendo uma analise estatistica
print(df.describe())

# --- Distribuição de idade ---
# Fazendo histograma usando dados da coluna Age
df.Age.hist(rwidth=0.9)

# Colocando legenda no eixo x
plt.xlabel("Idade")

# Colocando legenda no eixo y
plt.ylabel("Número de Profissionais")

# Colocando titulo no grafico
plt.title("Distribuição de Idade")

# Mostrando o grafico
plt.show()

# --- Distribuição de sexo ---
# Lista de generos
x = df.Gender.value_counts().index

# Quantas pessoas há de cada genero
y = df.Gender.value_counts().values

# Criando um grafico de barras passando x e y, definindo largura das barras, o alinhamento e as cores de cada barra.
plt.bar(x, y, width=0.5, align='center', color=['blue', 'pink', 'black', 'black', 'black'])

# Mostrando o grafico
plt.show()

# --- Distribuição de interesses ---
# Lista de cargos
x2 = df.JobRoleInterest.value_counts().index

# Quantas pessoas há em cada cargo
y2 = df.JobRoleInterest.value_counts().values

# Lista de cores
cores = ['OliveDrab', 'Orange', 'OrangeRed', 'DarkCyan', 'Salmon', 'Sienna', 'Maroon', 'LightSlateGrey', 'DimGray']

# Criando um grafico de barras passando x2 e y2, colocando o comprimento das barras,
# alinhando ao centro e definindo cores
plt.bar(x2, y2, width=0.9, align='center', color=cores)

# Funcao para girar legendas que estão no eixo x
plt.xticks(rotation=90)

# Mostrando o grafico
plt.show()

# Lista de categorias de empregos
x3 = df.EmploymentField.value_counts().index

# Quantas pessoas há em cada categoria
y3 = df.EmploymentField.value_counts().values

# Lista de cores
cores = ['OliveDrab', 'Orange', 'OrangeRed', 'DarkCyan', 'Salmon', 'Sienna', 'Maroon', 'LightSlateGrey', 'DimGray']

plt.bar(x3, y3, width=0.9, align='center', color=cores)

# Funcao para girar legendas que estão no eixo x
plt.xticks(rotation=90)

# Mostrando o grafico
plt.show()

# --- Preferências de trabalho por idade ---
# Guardando uma copia de df em df_ageranges
df_ageranges = df.copy()

# Use cut() quando precisar segmentar e classificar valores de dados em posições.
# Por exemplo, cut() pode converter idades em grupos de faixas etárias.
df_ageranges['AgeRanges'] = pd.cut(df_ageranges['Age'], bins=[10, 20, 30, 40, 50, 60, 70], labels=["< 20", "20-30", "30-40", "40-50", "50-60", "< 60"]) 

# crosstab(indice, valor)
# apply recebe uma função que será aplicada em cada coluna, nesse caso
df2 = pd.crosstab(df_ageranges.AgeRanges, df_ageranges.JobPref).apply(lambda r: r/r.sum(), axis=1)

# Lista de cores
cores = ['OliveDrab', 'Orange', 'OrangeRed', 'DarkCyan', 'Salmon', 'Sienna', 'Maroon', 'LightSlateGrey', 'DimGray']

# Traçando a variavel df2 em um grafico do tipo barra, empilhado, usando as cores da nossa lista e com um titulo
ax1 = df2.plot(kind="bar", stacked=True, color=cores, title="Preferência de Trabalho por Idade")

# legend() adiciona uma caixa com legendas
# bbox_to_anchor=() define a posição da caixa com legendas
ax1.legend(bbox_to_anchor=(1, 1))

# --- Realocação por idade ---
df3 = pd.crosstab(df_ageranges.AgeRanges, df_ageranges.JobRelocateYesNo).apply(lambda r: r/r.sum(), axis=1)

# Lista de cores
cores = ['OliveDrab', 'Orange', 'OrangeRed', 'DarkCyan', 'Salmon', 'Sienna', 'Maroon', 'LightSlateGrey', 'DimGray']

ax1 = df3.plot(kind="bar", stacked=True, color=cores, title="Realocação por Idade")

ax1.legend(["Não", "Sim"], loc='best', bbox_to_anchor=(1, 1))

# --- Idade x horas de aprendizagem ---
# Guardando uma copia de df em df9
df9 = df.copy()

# dropna() remove valores ausentes
df9 = df9.dropna(subset=["HoursLearning"])

# df['Age'].isin(range(0, 70)) -> Se os valores que estão na coluna Age estão entre 0 e 70
df9 = df9[df['Age'].isin(range(0, 70))]

# Definindo os valores de x e y
x = df9.Age
y = df9.HoursLearning

# polyfit() faz o ajuste polinomial de mínimos quadrados, faz uma linha de regressão.
m, b = np.polyfit(x, y, 1)

# Traçando os valores de x e y em forma de pontos
plt.plot(x, y, '.')

# Traçando linha vermelha
plt.plot(x, m * x + b, '-', color="red")

# Legenda para o eixo x
plt.xlabel("Idade")

# Legenda para o eixo y
plt.ylabel("Horas de Treinamento")

# Titulo para o grafico
plt.title("Idade por Horas de Treinamento")

# Mostrando o grafico
plt.show()

# Copia de df
df5 = df.copy()

# dropna() remove valores ausentes
df5 = df5.dropna(subset=["ExpectedEarning"])

# df['MoneyForLearning'].isin(range(0,60000)) -> Se os valores que estão na coluna MoneyForLearning estão entre 0 e 60000
df5 = df5[df['MoneyForLearning'].isin(range(0,60000))]

# Definindo os valores de x e y
x = df5.MoneyForLearning
y = df5.ExpectedEarning

m, b = np.polyfit(x, y, 1)
plt.plot(x, y, '.')
plt.plot(x, m*x + b, '-', color = "red")

# Colocando legenda no eixo x
plt.xlabel("Investimento em Treinamento")

# Colocando legenda no eixo y
plt.ylabel("Expectativa Salarial")

# Colocando um titulo no grafico
plt.title("Investimento em Treinamento vs Expectativa Salarial")

# Mostrando o grafico
plt.show()
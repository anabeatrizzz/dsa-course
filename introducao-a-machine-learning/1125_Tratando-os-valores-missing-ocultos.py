# Shared via Compiler App https://g633x.app.goo.gl/TPlw
from sklearn.preprocessing import Imputer

# valores missing: valores que faltam no conjunto de dados, NaN
# valores missing ocultos: quando não havia informação para aquela coluna e foi preenchida com zero

# Mostrando quantos valores 0 há em cada coluna
print("Linhas no dataframe {0}".format(len(df)))

print("Linhas missing glucose_conc: {0}".format(len(df.loc[df['glucose_conc'] == 0])))

print("Linhas missing diastolic_bp: {0}".format(len(df.loc[df['diastolic_bp'] == 0])))

print("Linhas missing thickness: {0}".format(len(df.loc[df['thickness'] == 0])))

print("Linhas missing insulin {0}".format(len(df.loc[df['insulin'] == 0])))

print("Linhas missing bmi: {0}".format(len(df.loc[df['bmi'] == 0])))

print("Linhas missing age: {0}".format(len(df.loc[df['age'] == 0])))

# Imputer() recebe o valor que deve ser substituído, a substituição e o eixo em que o valor está
preenche_zero = Imputer(missing_values=0, strategy="mean", axis=0)

# Fazendo a substituição nos conjuntos de dados X_treino e X_teste
X_treino = preenche_zero.fit_transform(X_treino)
X_teste = preenche_zero.fit_transform(X_teste)
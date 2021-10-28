from sklearn.model_selection import train_test_split

# Lista de colunas preditoras
atributos = ['num_preg', 'glucose_conc', 'diastolic_bp', 'thickness', 'insulin', 'bmi', 'diab_pred', 'age']

# Coluna que queremos prever
atrib_prev = ['diabetes']

# X representará os valores de cada coluna preditora
X = df[atributos].values

# Y representará os valores da coluna target
Y = df[atrib_prev].values

# Critério para fazer a divisão do conjunto de dados
split_test_size = 0.30

# Na função train_test_split() indicamos X e Y; o parametro test_size (o tamanho do conjunto de teste) recebe o critério de 0.30, assim, o conjunto de dados de treinamento terá 70% do conjunto de dados original
X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, Y, test_size=split_test_size, random_state=42)

print("{0:0.2f}% nos dados de treino".format((len(X_treino)/len(df.index)) * 100))
print("{0:0.2f}% nos dados de teste".format((len(X_teste)/len(df.index)) * 100))

# Quantas pessoas tem e não tem diabetes
# len(df.loc[df['diabetes'] == 1] --> quantidade de registros na coluna diabetes de df, que possuem valor igual a 1
# len(df.index) * 100 --> quantidade de linhas vezes 100 para fazer a porcentagem
print("Original True : {0} ({1:0.2f}%)".format(len(df.loc[df['diabetes'] == 1]), (len(df.loc[df['diabetes'] ==1]) / len(df.index) * 100)))

# len(df.loc[df['diabetes'] == 0] --> quantidade de registros na coluna diabetes de df, que possuem valor igual a 0
print("Original False : {0} ({1:0.2f}%)".format(len(df.loc[df['diabetes'] == 0]), (len(df.loc[df['diabetes'] == 0]) / len(df.index) * 100)))

# Quantas pessoas tem e não tem diabetes no conjunto de dados para treino
print("Training True : {0} ({1:0.2f}%)".format(len(Y_treino[Y_treino[:] == 1]), (len(Y_treino[Y_treino[:] == 1])/len(Y_treino) * 100)))

print("Training False : {0} ({1:0.2f}%)".format(len(Y_treino[Y_treino[:] == 0]), (len(Y_treino[Y_treino[:] == 0])/len(Y_treino) * 100)))

# Quantas pessoas tem e não tem diabetes no conjunto de dados para teste
print("Test True : {0} ({1:0.2f}%)".format(len(Y_teste[Y_teste[:] == 1]), (len(Y_teste[Y_teste[:] == 1])/len(Y_teste) * 100)))

print("Test False : {0} ({1:0.2f}%)".format(len(Y_teste[Y_teste[:] == 0]), (len(Y_teste[Y_teste[:] == 0])/len(Y_teste) * 100)))
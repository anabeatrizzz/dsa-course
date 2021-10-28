# Shared via Compiler App https://g633x.app.goo.gl/TPlw
# Importando
from sklearn.linear_model import LogisticRegression

# Criando um modelo de regressão logística
modelo_v3 = LogisticRegression(C=0.7, random_state=42)

# Treinando o modelo passando os dados de treino
modelo_v3.fit(X_treino, Y_treino.ravel())

# Fazendo previsão usando dados de teste
lr_predict_test = modelo_v3.predict(X_teste)

print("Exatidão (Accuracy): {0:.4f}".format(metrics.accuracy_score(Y_teste, lr_predict_test)))

print()

print("Classification Report")
print(metrics.classification_report(Y_teste, lr_predict_test, labels = [1, 0]))

# Fazendo Previsões Com o Modelo Treinado

# Importando
import pickle

# Variavel que guarda o nome do arquivo
filename = 'modelo_treinado_v3.sav'

# dump() serve para armazenar o objeto
# dump(nome_objeto, nome_arquivo_do_objeto)
# wb significa write-binary
pickle.dump(modelo_v3, open(filename, 'wb'))

# Guardando o arquivo
loaded_model = pickle.load(open(filename, 'rb'))

# Indicando que iremos prever apenas o valor que está na posição 15 de X_teste
resultado1 = loaded_model.predict(X_teste[15].reshape(1, -1))

# Indicando que iremos prever apenas o valor que está na posição 18 de X_teste
resultado2 = loaded_model.predict(X_teste[18].reshape(1, -1))

# O modelo previu, usando os dois valores, que o primeiro não tem diabetes e o segundo tem
print(resultado1)
print(resultado2)
# Shared via Compiler App https://g633x.app.goo.gl/TPlw
from sklearn import metrics

# Exatidão com dados de treino
# Na função predict() passamos os dados referentes a colunas preditoras
nb_predict_train = modelo_v1.predict(X_treino)

# Na função accuracy_score() passamos os dados de treino da coluna diabetes e também a previsão
print("Exatidão (Accuracy): {0:.4f}".format(metrics.accuracy_score(Y_treino, nb_predict_train)))

# Exatidão com dados de teste
nb_predict_test = modelo_v1.predict(X_teste)

print("Exatidão (Accuracy): {0:.4f}".format(metrics.accuracy_score(Y_teste, nb_predict_test)))
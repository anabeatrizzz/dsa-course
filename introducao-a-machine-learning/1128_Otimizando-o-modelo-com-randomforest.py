# Shared via Compiler App https://g633x.app.goo.gl/TPlw
# Importando
from sklearn.ensemble import RandomForestClassifier

# Criando modelo
modelo_v2 = RandomForestClassifier(random_state=42)

# Treinando modelo
modelo_v2.fit(X_treino, Y_treino.ravel())

# Prevendo dados de treino relacionados com o tamanho das casas
rf_predict_train = modelo_v2.predict(X_treino)

# Mostrando exatidão com os dados de treino relacionados com o preço das casas e os dados de rf_predict_train
print("Exatidão (Accuracy): {0:.4f}".format(metrics.accuracy_score(Y_treino, rf_predict_train)))

# Fazendo o mesmo com os dados de teste
rf_predict_test = modelo_v2.predict(X_teste)

print("Exatidão (Accuracy): {0:.4f}".format(metrics.accuracy_score(Y_teste, rf_predict_test)))

print("Confusion Matrix")

print("{0}".format(metrics.confusion_matrix(Y_teste, rf_predict_test, labels = [1, 0])))
print("")

print("Classification Report")
print(metrics.classification_report(Y_teste, rf_predict_test, labels = [1, 0]))

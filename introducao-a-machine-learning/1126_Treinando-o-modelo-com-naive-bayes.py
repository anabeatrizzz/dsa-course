# Shared via Compiler App https://g633x.app.goo.gl/TPlw
# GaussianNB é o algoritmo de Machine Learning. Há vários algoritmos no pacote naive_bayes
from sklearn.naive_bayes import GaussianNB

# Instanciando um objeto de GaussianNB
modelo_v1 = GaussianNB()

# Treinando o modelo passando os conjuntos de dados para treino
# ravel() conserta o shape
modelo_v1.fit(X_treino, Y_treino.ravel())
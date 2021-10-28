from sklearn.linear_model import LinearRegression

# Representando diametros de pizzas
X = [[7], [10], [15], [30], [45]]

# Representando preços de pizzas
Y = [[8], [11], [16], [38.5], [52]]

# Criando um modelo
modelo = LinearRegression()

# Treinando os valores de diametros e preços
modelo.fit(X, Y)

# Prevendo o preço se caso a pizza tivesse 20 de diametro
print(modelo.predict([[20]]))
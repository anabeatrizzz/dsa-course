import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
# tf.disable_v2_behavior()
# tf.compat.v1.Session()
# tf.compat.v1.disable_eager_execution()

# taxa_aprendizado
learning_rate = 0.01
# periodos_de_treino (acho que é para cada tamanho e preço)
training_epochs = 2000
# passo_de_amostra
display_step = 200

# Conjunto de dados de treino
# Tamanho das casas - dados para alimentar o modelo
train_X = np.asarray([
    3.3, 4.4, 5.5, 6.71, 6.93,
    4.168, 9.779, 6.182, 7.59, 2.167,
    7.042, 10.791, 5.313, 7.997, 5.654,
    9.27, 3.1])

# Preço das casas - dados para alimentar o modelo
train_y = np.asarray([
    1.7, 2.76, 2.09, 3.19, 1.694,
    1.573, 3.366, 2.596, 2.53, 1.221,
    2.827, 3.465, 1.65, 2.904, 2.42,
    2.94, 1.3])

# n_samples recebe apenas a quantidade de linhas de train_X
n_samples = train_X.shape[0]
 
# Conjunto de dados de teste
# Tamanho das casas - dados para testar o modelo e ele retornar uma previsão
test_X = np.asarray([
    6.83, 4.668, 8.9, 7.91,
    5.7, 8.7, 3.1, 2.1])

# Preço das casas - dados para testar o modelo e ele retornar uma previsão
test_y = np.asarray([
    1.84, 2.273, 3.2, 2.831,
    2.92, 3.24, 1.35, 1.03])

# Placeholders para quando os tamanhos e preços das casas forem previstos
X = tf.compat.v1.placeholder(tf.float32)
y = tf.compat.v1.placeholder(tf.float32)
print(X)
 
# Pesos 
W = tf.Variable(np.random.randn(), name="weight")
# bias signfica viés que significa tendência ou carácter de algo.
b = tf.Variable(np.random.randn(), name="bias")

# Construindo o modelo linear
# Fórmula do modelo linear: y = W * X + b
linear_model = W * X + b
 
# Mean squared error (erro quadrado médio)
# reduce_sum() computa a soma dos elementos ao longo das dimensões de um tensor
# square() faz a multiplicação de um numero por ele mesmo
# Nesta equação, linear_model é a previsão e y é o valor real, então comparamos esses dois valores
# e iremos ter uma taxa de erro que é colocada em cost
cost = tf.reduce_sum(tf.square(linear_model - y)) / (2 * n_samples)
 
optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Variavel que será usada para iniciar as variaveis
init = tf.compat.v1.global_variables_initializer()
 
# Com a sessão aberta como sess
with tf.compat.v1.Session() as sess:
    # Execute as variaveis
    sess.run(init)
    # Para cada coisa em training_epochs
    for epoch in range(training_epochs):
        # Execute optimizar e passe valores para X e y
        sess.run(optimizer, feed_dict={X: train_X, y: train_y})
        # Para os numeros pares:
        if (epoch+1) % display_step == 0:
            # Execute o cost e passe valores para X e y
            c = sess.run(cost, feed_dict={X: train_X, y: train_y})
            print(f"Periodo: {epoch+1:6}\tCusto: {c:10.4}\tPeso: {sess.run(W):6.4}\tTendencia: {sess.run(b):6.4}")
    
    print("\nOtimização Concluída!")
    training_cost = sess.run(cost, feed_dict={X: train_X, y: train_y})
    print(f"Custo Final: {training_cost}", f" - Peso Final: {sess.run(W)}", f" - Tendencia Final: {sess.run(b)}", '\n')
    
    plt.figure(figsize=(10, 10))
    plt.plot(train_X, train_y, 'ro', label='Dados Originais')
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Linha de Regressão')
    plt.legend()
    plt.show()
    
    testing_cost = sess.run(tf.reduce_sum(tf.square(linear_model - y)) / (2 * test_X.shape[0]), feed_dict={X: test_X, y: test_y})
     
    print(f"Custo Final em Teste: {testing_cost}")
    print(f"Diferença Média Quadrada Absoluta: {abs(training_cost - testing_cost)}")
    
    plt.figure(figsize=(10, 10))
    plt.plot(test_X, test_y, 'bo', label='Dados de Teste')
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Linha de Regressão')
    plt.legend()
    plt.show()
    
sess.close()
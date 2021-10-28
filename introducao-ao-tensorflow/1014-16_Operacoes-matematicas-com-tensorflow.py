import tensorflow as tf

# Operações Matemáticas com Tensores
# Soma
# Linha adicionada por causa do erro
tf.disable_v2_behavior()

# Variavel com constante do TF do tipo int
node1 = tf.constant(5, dtype=tf.int32)

# Variavel com constante do TF do tipo int
node2 = tf.constant(9, dtype=tf.int32)

# Definindo soma entre node1 e node2
node3 = tf.add(node1, node2)

# Com sessão aberta como sess
with tf.compat.v1.Session() as sess:
    # Mostre a sessao executando node3
    print("A soma do node1 com o node2 é:", sess.run(node3))
    
# Subtração
# Tensor com valores aleatorios
# Com distruição normal
a = tf.random_normal([3])

# Com distribuição uniforme
b = tf.random_uniform([3])

# Definindo uma subtração entre a e b
subt = tf.subtract(a, b)

# Com sessão aberta como sess
with tf.compat.v1.Session() as sess:
    # Mostre os valores de a
    print('Tensor a: ', sess.run(a))
    # Mostre os valores de b
    print('\nTensor b: ', sess.run(b))
    # Mostre a subtração
    print('\nSubtração entre os 2 tensores é: ', sess.run(subt))
    
# Divisão
# Constantes com numero inteiro
no1 = tf.constant(21, dtype=tf.int32)
no2 = tf.constant(7, dtype=tf.int32)
# Definindo uma divisão entre no1 e no2
div = tf.div(no1, no2)
# Com sessão aberta como sess
with tf.compat.v1.Session() as sess:
    # Mostre a divisão
    print('Divisão entre os 2 tensores é: ', sess.run(div))
    
#Multiplicação
tf.compat.v1.disable_eager_execution()

# Matriz 1x2
tensor_a = tf.constant([[4, 2]])

# Matriz 2x1
tensor_b = tf.constant([[3],[7]])

# Definindo uma multiplicação entre tensor_a e tensor_b
prod = tf.multiply(tensor_a, tensor_b)

# Com sessão aberta como sess
with tf.compat.v1.Session() as sess:
    # Mostre os dados de tensor_a
    print('tensor_a: \n', sess.run(tensor_a))
    # Mostre os dados de tensor_b
    print('\ntensor_b: \n', sess.run(tensor_b))
    # Mostre a multiplicação entre os numeros de cada matriz
    print('\nProdut: \n', sess.run(prod))
    
# Linhas: Quantidade de pares de conchetes
# Colunas: Quantidade de elementos dentro dos conchetes

# Matriz 3x2
mat_a = tf.constant([[2, 3], [9, 2], [4, 5]])

# Matriz 2x3
mat_b = tf.constant([[6, 4, 5], [3, 7, 2]])

# A diferença entre matmul e multiply é que pode ser colocado mais parametros em matmul
# e essa função retorna um tensor com a quantidade de linhas de mat_a e a quantidade de colunas de mat_b
# mas as duas fazem multiplicação
mat_prod = tf.matmul(mat_a, mat_b)

# Com sessão aberta como sess
with tf.compat.v1.Session() as sess:
    # Mostre os dados de mat_a
    print('Tensor mat_a: \n', sess.run(mat_a))
    # Mostre os dados de mat_b
    print('\nTensor mat_b: \n', sess.run(mat_b))
    # Multiplicação entre os cada numero
    print('\nProduto: \n', sess.run(mat_prod))
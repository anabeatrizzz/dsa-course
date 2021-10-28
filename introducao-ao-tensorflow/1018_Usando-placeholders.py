import tensorflow as tf

# A função placeholder() é util quando não sabemos quais dados o tensor irá ter mas precisamos inicializá-lo.
# Como se fosse uma matriz de numeros inteiros 3x1 vazia, nesse caso
a = tf.compat.v1.placeholder(tf.int32, shape=(3, 1))
b = tf.compat.v1.placeholder(tf.int32, shape=(1, 3))

# Definindo uma multiplicação entre a e b
c = tf.matmul(a, b)

# Com uma sessão aberta como sess
with tf.compat.v1.Session() as sess:
    # A função feed_dict() nos ajuda a adicionar os dados, agora que já sabemos
    print(sess.run(c, feed_dict={a:[[3], [2], [1]], b:[[1, 2, 3]]}))
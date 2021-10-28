import tensorflow as tf

# Com uma sessão aberta como sess
with tf.compat.v1.Session() as sess:
    # Tensor constante que contem texto
    ola = tf.constant("Ola mundo")
    # Mostre a sessão executando o tensor
    print(sess.run(ola))
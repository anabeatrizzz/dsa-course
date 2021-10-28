import tensorflow as tf
tf.compat.v1.disable_eager_execution()

# Variavel com uma matriz 2x2 de zeros
node = tf.Variable(tf.zeros([2, 2]))

# Com uma sessão aberta como sess
with tf.compat.v1.Session() as sess:
    # Execute na sessão a função que incia variaveis
    sess.run(tf.compat.v1.global_variables_initializer())
    # Mostre os dados de node
    print("Tensor Original:\n", sess.run(node))
    # Use a função assign() para fazer uma atribuição, some node com uma matriz 2x2 preenchida com uns
    node = node.assign(node + tf.ones([2,2]))
    # Mostre node depois da atribuição
    print("\nTensor depois da adição:\n", sess.run(node))
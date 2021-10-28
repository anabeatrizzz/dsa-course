import matplotlib.pyplot as plt
import numpy as np

# Scatter é um grafico de dispersão
# Criando um grafico de dispersão passando um array numerico de 0 a 49 para o eixo x
# e 50 numeros aleatorios para o eixo y
plt.scatter(np.arange(50), np.random.randn(50))

# Mostrando o grafico
plt.show()

figura = plt.figure()

             # add_subplot(linhas, colunas, index)
eixo1 = figura.add_subplot(1, 2, 1)

# plot significa traçar
    # plot(valores_para_x, outros_parametros_opcionais)
eixo1.plot(np.random.randn(50), color="m")

eixo2 = figura.add_subplot(1, 2, 2)

    # scatter(valores_para_x, valores_para_y, outros_parametros_opcionais)
eixo2.scatter(np.arange(50), np.random.randn(50), color="r")

plt.show()

# Criando quatro graficos
_, plote = plt.subplots(2, 2)

plote[0,1].plot(np.random.randn(50), color="r", linestyle="--")
plote[0,0].bar(np.arange(10), np.arange(10), color="k", linestyle="-")
plote[1,1].scatter(np.random.randn(30), np.arange(30), color="b", linestyle=":")
plote[1,0].pie(np.random.rand(10))

plt.show()
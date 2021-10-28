import matplotlib as mpl
import matplotlib.pyplot as plt

# Fazendo e mostrando um grafico com coordenadas 1, 3, 5 para x e 2, 5, 7 para y
plt.plot([1, 3, 5], [2, 5, 7])
plt.show()

# Criando listas com coordenadas
x = [1, 2, 3]
y = [4, 5, 6]

# Fazendo um grafico passando as listas como parametro
plt.plot(x, y)

# Criando uma legenda para o eixo x
plt.xlabel("Variavel 1")

# Criando uma legenda para o eixo y
plt.ylabel("Variavel 2")

# Criando um titulo para o grafico
plt.title("Teste")

# Mostrando o grafico
plt.show()

# Criando novas listas com coordenadas
x2 = [7, 8, 9]
y2 = [-1, -8, -3]

# Fazendo um grafico passando as novas listas como parametro e definindo uma legenda para a linha
plt.plot(x2, y2, label="Linha")
plt.legend()

# Mostrando o grafico
plt.show()
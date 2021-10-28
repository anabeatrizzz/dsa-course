import matplotlib as mpl
import matplotlib.pyplot as plt

# Criando listas com coordenadas
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

# Chamando função bar para criar um grafico de barras,
# passando as listas como parametro, criando legenda e definindo cor
plt.bar(x, y, label="Barras", color="r")
plt.legend()

# Mostrando grafico de barras
plt.show()

x2 = [-1, -2, -3]
y2 = [1, 2, 3]

# Começando da direita para a esquerda
plt.bar(x2, y2, label="Barras 1", color="m")

# Começando da esquerda para a direita
plt.bar(x, y, label="Barras 2", color="y")
plt.legend()
plt.show()

idades = [22, 65, 45, 55, 21, 22, 34, 42, 41, 4, 99, 101, 120, 122, 130, 111, 115, 80, 75, 54, 44, 64, 13, 18, 48]
ids = [x for x in range(len(idades))]

plt.bar(ids, idades)
plt.show()
# Ou seja, ids representa os numeros de 0 até 24 pois há essa quantidade dentro de idades
# valores de ids serão eixo x e valores de idades serão eixo y

bills = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Criando e mostrando um histograma
plt.hist(idades, bills, histtype="bar", rwidth=0.8)
plt.show()

x3 = [1, 5, 8]
y3 = [6, 9, 3]

# marker: forma do marcador.
# s: tamanho do marcador.
plt.scatter(x3, y3, label="Pontos", color="g", marker="*", s=200)
plt.legend()
plt.show()

semana = [x for x in range(1, 8)]
mes = [x for x in range(2, 9)]
dia = [x for x in range(3, 10)]

plt.stackplot(semana, mes, dia, colors=["r", "m", "g"])
plt.show()

# Criando parametros para a função pie()
fatias = [2, 2, 2]
atividades = ["correr", "dormir", "tomar banho"]
colunas = ["r", "g", "m"]

# Criando e mostrando um grafico de barras
plt.pie(fatias, labels=atividades, colors=colunas, shadow=True)
plt.show()
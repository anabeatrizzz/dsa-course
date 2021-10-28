import matplotlib as mpl
import matplotlib.pyplot as plt
from pylab import *

  # linspace(começo, fim, quantidade)
x = linspace(0, 5, 10)
y = x ** 2

# Criando uma figura
figura = plt.figure()

# Define o tamanho da figura
eixos = figura.add_axes([0.5, 0.5, 0.5, 0.5])

# Colocando valores e cor nos eixos do grafico
eixos.plot(x, y, "m")

# Colocando legendas e titulo nos eixos do grafico
eixos.set_xlabel("X")
eixos.set_ylabel("Y")
eixos.set_title("Grafico de linha")

# Criando dois graficos na mesma figura
x2 = linspace(0, 5, 10)
y2 = x ** 2

# Criando a figura
figura2 = plt.figure()

# Criando eixos para os dois graficos
eixos2 = figura2.add_axes([0.7, 0.6, 0.7, 0.6])
eixos3 = figura2.add_axes([0.2, 0.5, 0.4, 0.3])

# Colocando valores nos eixos e definindo cor
eixos2.plot(x2, y2, "r")

# Colocando legendas nos eixos e no titulo
eixos2.set_xlabel("X")
eixos2.set_ylabel("Y")
eixos2.set_title("Grafico 1")

# Colocando valores nos eixos e definindo cor
eixos3.plot(y2, x2, "g")

# Colocando legendas nos eixos e no titulo
eixos3.set_xlabel("Y")
eixos3.set_ylabel("X")
eixos3.set_title("Grafico 2")

# figura é do tipo figura do matplotlib
# eixos é do tipo array do numpy
figura, eixos = plt.subplots(nrows = 1, ncols = 2)
for c in eixos:
    c.plot(x2, y2, "r")
    c.set_xlabel("X")
    c.set_ylabel("Y")
    c.set_title("Grafico")
    
figura.tight_layout()
import math

print(dir(math))
# Vendo todos os metodos que a biblioteca math possui

print(math.sqrt(25))
# Resulta na raiz quadrada de 25

from math import sqrt
# Podemos especificar qual metodo queremos da biblioteca math

sqrt(9)

help(sqrt)
# Se nao sabemos o que algum metodo faz, colocamos o nome dele nos parenteses do metodo help()

import random

random.choice(["A", "B", "C", "D", "E"])
# O metodo choice escolhe um valor aleatorio que esta dentro da lista

random.sample(range(100), 10)
# O metodo sample mostra 10 numeros que estao entre 0 a 100

import statistics

dados = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(statistics.mean(dados))
# O metodo mean faz a media dos numeros que estao dentro da lista dados

print(statistics.median(dados))
# O metodo median faz a mediana dos numeros que estao dentro da lista dados

import urllib.request
resposta = urllib.request.urlopen("http://python.org")
# A funcao urlopen abre um site da internet e armazena ele em resposta

html = resposta.read()
print(html)
# Quando lemos um site, é mostrado o html dele
import numpy as np

# Criando uma matriz.
matriz = np.array([[1, 2, 3], [4, 5, 6]])

# Mostrando a matriz.
print(matriz)

# Mostrando quantas linhas e colunas essa matriz possui.
print(matriz.shape)

print("\n")
# Criando uma matriz 2x3 preenchida com 1s.
matriz1 = np.ones((2, 3))

# Mostrando essa matriz 2x3.
print(matriz1)

print("\n")
# Uma lista possuindo 3 listas.
lista = [[2, 4], [6, 8], [10, 12]]

# Transformando essa lista em uma matriz.
matriz2 = np.matrix(lista)

# Mostrando essa matriz.
print(matriz2)

# Mostrando quantas linhas e colunas essa matriz possui.
print(np.shape(matriz2))

# Mostrando quantos elementos há na matriz
print(matriz2.size)

# Mostrando o tipo de dado dessa matriz.
print(matriz2.dtype)

# Verificando o tamanho de cada elemento.
print(matriz2.itemsize)

# Mostrando o total de bytes da matriz.
print(matriz2.nbytes)

# Mostrando o elemento que está na posição linha 0, coluna 0
print(matriz2[0, 0])

# Mudando o valor do elemento que está na posição linha 0, coluna 0 para 100
matriz2[0, 0] = 100

# Mostrando a matriz com as alterações.
print(matriz2)

print("\n")
# Mesmo escrevendo numeros inteiros nesse vetor, podemos estabelecer o tipo de dado dele usando dtype.
x = np.array([1, 2], dtype=np.float64)

# Mostrando o tipo de dado do vetor.
print(x.dtype)

print("\n")
# Criando uma matriz e estabelecendo que ela é do tipo float.
matriz3 = np.array([[14, 16], [18, 20]], dtype=float)

# Mostrando o numero de dimensões da matriz.
print(matriz3.ndim)
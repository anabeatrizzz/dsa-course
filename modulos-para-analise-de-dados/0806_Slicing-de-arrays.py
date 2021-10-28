import numpy as np

print("\033[33mCriando e mostrando uma matriz com diagonais numericas de 0 até 2:\033[m")
a = np.diag(np.arange(3))
print(a)

print("\n\033[33mMostrando o elemento que está na linha 1 coluna 1:\033[m")
print(a[1, 1])

print("\n\033[33mMostrando valores da linha com indice 1:\033[m")
print(a[1])

print("\n\033[33mCriando e mostrando um vetor com valores de 0 até 9:\033[m")
b = np.arange(10)
print(b)

print("\n\033[33mComeçando do indice 2 e indo até o indice 9, mostre os valores pulando de 3 em 3\033[m")
print(b[2:9:3])

print("\n\033[33mMostrando se os dois arrays são iguais:\033[m")
print(np.array_equal(a, b))

print("\n\033[33mMostrando o valor minimo e maximo de uma array:\033[m")
print(a.min())
print(a.max())

print("\n\033[33mMostrando a soma de 10 com cada elemento dentro da array:\033[m")
print(np.array([1, 2, 3]) + 10)

print("\n\033[33mCriando um vetor e mostrando o arredondamento de cada elemento dentro dele:\033[m")
array = np.array([1.5, 1.6, 2.8, 3.1])
print(np.around(array))

print("\n\033[33mCriando e copiando um array:\033[m")
B = np.array([1, 2, 3, 4])
C = B.flatten()
print(C)


v = np.array([1, 2, 3])
# new axis = novo eixo
# (eixo X, eixo Y)
# Ou seja, está mostrando todos os elementos no eixo Y pois, não há um newaxis no lugar do eixo X (espero que minha eu do futuro entenda este raciocinio)
print("\n\033[33mMostrando o vetor criado horizontalmente:\033[m")
print(v[:, np.newaxis])

# Os valores do vetor foram invertidos, agora estão na horizontal
# O shape retorna (quantidade de linhas, quantidade de colunas)
print("\n\033[33mMostrando quantidade de linhas e colunas desse vetor horizontal:\033[m")
print(v[:,np.newaxis].shape)

print("\n\033[33mRepetindo o primeiro, depois o segundo... valores 2 vezes:\033[m")
print(np.repeat(v, 2))

print("\n\033[33mRepetindo o primeiro, junto com o segundo... valores 2 vezes:\033[m")
print(np.tile(v, 2))

outro = np.array([5, 6])

print("\n\033[33mJuntando uma array com outra:\033[m")
print(np.concatenate((v, outro), axis=0))

print("\n\033[33mOutra maneira de copiar uma array:\033[m")
r = np.copy(v)
print(r)
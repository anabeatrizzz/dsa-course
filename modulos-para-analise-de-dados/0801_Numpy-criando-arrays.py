import numpy as np

# Criando um array. Array apenas tem valores do mesmo tipo.
vetor1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

# Faz a soma acumulada.
# 0 + 0, 1 + 0, 2 + 1 + 0...
print(vetor1.cumsum())

# Mostra apenas quantos elementos há no vetor.
# Se fosse uma matriz, haveria outro numero depois da virgula.
print(vetor1.shape)
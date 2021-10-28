import numpy as np

A = np.array([10, 20, 30, 40])

# A média da array A (soma todos os numeros e divide pela quantidade de elementos dentro da array)
print(np.mean(A))

# O desvio padrão mostra o quanto de variação ou "dispersão" existe em relação à média (ou valor esperado). Um baixo desvio padrão indica que os dados tendem a estar próximos da média. Um desvio padrão alto indica que os dados estão espalhados por uma gama de valores.
print(np.std(A))

# Variância é uma medida da sua dispersão estatística, indicando "o quão longe" em geral os seus valores se encontram do valor esperado
print(np.var(A))

# Criando uma array com numeros de 1 a 9
d = np.arange(1, 10)

# Mostrando essa array
print(d)

# Mostrando a soma de todos os elementos dentro da array
print(np.sum(d))

# Mostra o resultado da multiplicação de todos os elementos dentro da array.
print(np.prod(d))

# Mostra a soma acumulada de todos os elementos dentro da array.
print(np.cumsum(d))
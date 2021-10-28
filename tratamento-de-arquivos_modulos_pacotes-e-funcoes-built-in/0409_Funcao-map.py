def fa(temperatura):
  return (9.0 / 5) * temperatura + 32


def ce(temperatura):
  return (5.0 / 9) * (temperatura - 32)


temperaturas = [1, 2, 3, 4, 5]

print()
print(list(map(fa, temperaturas)))
# Sintaxe dessa função: map(funcao, sequencia)
# Ou seja, a função fa será feita utilizando cada item dentro da lista temperaturas.
# Temos que fazer a conversão para lista, se não, iremos receber um iterador.
print()
for c in map(fa, temperaturas):
  print(c)

print()
print(list(map(ce, temperaturas)))

print()
print(list(map(lambda x: (5.0 / 9) * (x - 32), temperaturas)))

print()
# Somando elementos de duas listas:
a = [1, 2, 3]
b = [3, 2, 1]
print(list(map(lambda x, y: x + y, a, b)))

print()
# Somando elementos de tres listas:
c = [4, 5, 6]
d = [7, 8, 9]
e = [6, 5, 4]
print(list(map(lambda x, y, z: x + y + z, c, d, e)))
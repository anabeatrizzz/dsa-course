# A função reduce permite a redução de uma lista de elementos, assim, só um valor é retornado.

def soma(a, b):
  x = a + b
  return x


from functools import reduce
lista = [1, 2, 3]

print(
  reduce(soma, lista)
)

print()
print(
  reduce(lambda x, y: x + y, lista)
)

print()
maximo = lambda c, d: c if (c > d) else d
print(
  reduce(maximo, lista)
)
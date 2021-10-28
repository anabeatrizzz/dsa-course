# A função filter recebe uma função booleana e uma sequencia. Apenas mostrará os valores da sequencia se o resultado for True

def par(numero):
  if numero % 2 == 0:
    return True
  else:
    return False


lista = [0, 1, 2, 3, 4, 5]
print(
  list(
    filter(par, lista))
)

print()
print(
  list(
    filter(lambda x: x % 2 == 0, lista)
  )
)

print()
print(
  list(
    filter(lambda numero: numero < 4, lista)
  )
)
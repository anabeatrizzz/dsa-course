# A funcao enumerate apenas retorna a posicao e o valor que esta nessa posicao
sequencia = ["a", "b", "c"]
list(
    enumerate(sequencia)
)

print()
for i, v in enumerate(sequencia):
    print(i, v)

print()
for i, v in enumerate(sequencia):
    if i >= 2:
        break
    else:
        print(v)

print()
lista = ["Ana", "Beatriz", "Augusto"]
for indice, item in enumerate(lista):
    print(indice, item)

print()
for indice, item in enumerate("Texto"):
    print(indice, item)

print()
for indice, item in enumerate(range(5)):
    print(indice, item)
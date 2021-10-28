# A funcao zip une duas sequencias e retorna uma nova sequencia.
x = [1, 2, 3]
y = [4, 5, 6]
list(
    zip(x, y)
)
print()
list(
    zip("ABCD", "xy")
)
print()
a = [1, 2, 3]
b = [4, 5, 6, 7, 8]
list(
    zip(a, b)
)
print()
d1 = {"a": 1, "b": 2}
d2 = {"c": 4, "d": 5}
list(
    zip(d1, d2)
)
print()
list(
    zip(d1, d2.values()
    )
)
print()
def troca(dicionario1, dicionario2):
    dicionario_temporario = {}
    for c, v in zip(dicionario1, dicionario2.values()):
    dicionario_temporario[c] = v
return dicionario_temporario
troca(d1, d2)
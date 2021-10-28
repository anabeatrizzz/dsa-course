lista = [c for c in "python"]
print(lista)
# Mostre cada caracter dentro da palavra 'python'

print()
lista2 = [c for c in range(11) if c % 2 == 0]
print(lista2)
# Leitura: Para cada numero de 0 até 10, se os numeros forem pares, os mostre na tela.

print()
lista3 = [1, 2, 3, 4, 5]
fa = [((9.0 / 5) * c + 32) for c in lista3]
print(fa)
# Leitura: Aplique a conta, substituindo c por cada item dentro da lista3, mostrando os resultados dentro de outra lista.

print()
lista4 = [c ** 2 for c in [c ** 2 for c in range(11)]]
# Leitura:
# [c ** 2 for c in range(11)]
# Multiplique por 2 todos os numeros de 0 a 10
# Ou seja: 0, 1, 4, 9...

# [c ** 2 for c in ...]
# Multiplique de novo, por 2, os numeros ja multiplicados
# Resultado: 0, 1, 16, 81...
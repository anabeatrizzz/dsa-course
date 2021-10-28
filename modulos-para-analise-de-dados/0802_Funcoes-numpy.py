import numpy as np

# Sintaxe: arange(inicio, fim, passo)
# Similar ao range: for c in range(1, 10, 2):
print("\n")
vetor2 = np.arange(0, 50, 5)
print(vetor2)
print(
  np.shape(vetor2)
)

# Mostra o tipo de dado do vetor
print("\n")
print(vetor2.dtype)

# Vetor de 0 a 10 pulando de 2 em 2:
print("\n")
print(np.arange(0, 10, 2))

# Vetor preenchido com zeros:
print("\n")
print(np.zeros(5))

# Matriz com 1 nas diagonais e 0 nas posições restantes
print("\n")
print(np.eye(3))

# Passando numeros para as diagonais da matriz:
print("\n")
print(
  np.diag(
    np.array(
      [1, 2, 3]
    )
  )
)

# Array de numeros complexos:
print("\n")
print(
  np.array(
    [1+2j, 3+4j]
  )
)

# Array de valores booleanos:
print("\n")
print(
  np.array(
    [True, False, True, False]
  )
)

# Array de strings:
print("\n")
print(
  np.array(["Ana", "Beatriz", "Augusto"])
)

# Array de numeros entre 0 e 2:
print("\n")
print(np.linspace(0, 2))

#lista = [10]
#print(list(map(lambda x: 2 ** (2 ** x), lista)))
#import numpy as np

#r = np.arange(0, 10)
#print(list(map(lambda x: 2 ** (2 ** x), r)))
#print(r)
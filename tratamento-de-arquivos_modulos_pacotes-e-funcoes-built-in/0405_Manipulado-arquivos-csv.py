# Manipulando arquivos CSV:

import csv
with open("numeros.csv", "w") as arquivo:
  escrever = csv.writer(arquivo)
  escrever.writerow(("primeira", "segunda", "terceira"))
  escrever.writerow((10, 20, 30))
  escrever.writerow((40, 50, 60))
print()
with open("numeros.csv", "r") as arquivo:
  ler = csv.reader(arquivo)
  for c in ler:
    print("Numero de colunas: ", len(c))
    print(c)
print()
with open("numeros.csv", "r") as arquivo:
  ler = csv.reader(arquivo)
  dados = list(ler)
print(dados)
print()
for c in dados:
  print(c)
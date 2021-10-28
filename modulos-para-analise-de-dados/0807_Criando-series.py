import pandas as pd

print("\033[33mUma série é como se fosse uma tabela contendo indices e valores.\033[m")
# Criando uma serie
serie1 = pd.Series([10, 20, 30])
# Mostrando a serie
print(serie1)

print("\n\033[33mMostrando valores e indices da série criada:\033[m")
print(serie1.values)
print(serie1.index)

print("\n\033[33mPodemos definir os indices da serie também:\033[m")
serie2 = pd.Series([40, 50, 60, 13], index = ['A', 'B', 'C', 'D'])
print(serie2)
# Mostrando indices dessa segunda serie:
print(serie2.index)

print("\n\033[33mMostrando tudo que é menor que 50 na serie:\033[m")
print(serie2[serie2 < 50])

print("\n\033[33mMostrando tudo que está no indice B:\033[m")
print(serie2["B"])

print("\n\033[33mDizendo se o indice D está presente na serie:\033[m")
print("D" in serie2)
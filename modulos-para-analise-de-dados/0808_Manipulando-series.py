import pandas as pd

# Criando um dicionario
dicionario = {"Nome":"Ana Beatriz", "Idade": 18, "Signo": "Libra", "Profissão":"Estudante"}
# Passando este dicionario como parametro para o metodo Series e guardando em serie3
serie3 = pd.Series(dicionario)
# Mostrando a serie
print(serie3)

print("\n")

# Criando uma lista
lista = ["Nome", "Idade", "Signo", "Branco"]
# Os indices serão os textos que estão dentro de lista e os valores serão os valores que estão em dicionario
serie4 = pd.Series(dicionario, index=lista)
# Não foi encontrado uma relação indice - valor então fica preenchido com NaN
print(serie4)

print("\n")

# Há algum valor nulo em serie4?
print(pd.isnull(serie4))
# Há algum valor não-nulo em serie4?
print(pd.notnull(serie4))

print("\n")

# Primeiro o pandas busca se há uma relação depois soma os valores
print(serie3 + serie4)
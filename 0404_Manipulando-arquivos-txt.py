# Manipulando arquivos .txt:

texto = "Ana\n"
texto += "Beatriz\n"
texto += "Augusto"
import os
arquivo = open(os.path.join("nome.txt"), "w")
for c in texto.split():
    arquivo.write(c + " ")
arquivo.close()
arquivo = open("nome.txt", "r")
conteudo = arquivo.read()
arquivo.close()
print(conteudo)

# Usando expressão with:

with open("nome.txt", "r") as arquivo:
    conteudo = arquivo.read()
print(conteudo)

with open("nome.txt", "w") as arquivo:
    arquivo.write(texto[:10])
    arquivo.write("\n")
    arquivo.write(texto[:15])
arquivo = open("nome.txt", "r")
conteudo = arquivo.read()
arquivo.close()
print(conteudo)
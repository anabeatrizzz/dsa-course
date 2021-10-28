class Livros():
    def __init__(self, title, numero):
    # self é uma referencia a cada atributo da classe Livros (titulo e isbn)
    # Esta funcao tambem é chamada de construtora pois, inicia a classe.
        self.titulo = title
        self.isbn = numero
        print("Construtor identificado.")
    def imprime(self, title, numero):
        print("Foi criado o livro {} com ISBN {}".format(title, numero))


livro2 = Livros("Os tres porquinhos", 6789)
# Quando um objeto é criado, é checado na classe dele se na funcao construtora há algo para executar. Neste caso há uma mensagem a ser mostrada.
# Escrevemos dois parametros pois, criamos mais dois, além de self nas linhas 2 e 8.

print()
print(livro2.titulo)
# Mostrando o que o atributo titulo recebe, no caso, um texto.

print()
livro2.imprime("Os tres porquinhos", 6789)
# Executando a segunda funcao da classe Livros.

class Cachorros():
    def __init__(self, r):
        self.raca = r
        print()
        print("Construtor identificado.")


Lilica = Cachorros("Vira-Lata")

print()
print(Lilica.raca)
class Livros():
    def __init__(self):
    # self é uma referencia a cada atributo da classe Livros (titulo e isbn)
    # Esta funcao tambem é chamada de construtura pois, inicia a classe
        self.titulo = "As 32 leis do sucesso"
        self.isbn = 12345
        print("Construtor identificado")
    def imprime(self):
        print("Foi criado o livro {} com ISBN {}".format(self.titulo, self.isbn))


livro1 = Livros()
# Quando um objeto é criado, é checado na classe dele se na funcao construtura há algo para executar. Neste caso há uma mensagem a ser mostrada.

print()
print(livro1.titulo)
# Mostrando o que o atributo titulo recebe, no caso, um texto.

print()
livro1.imprime()
# Executando a segunda funcao da classe Livros.
class Livros():
    def __init__(self, t, a, p):
        print("Livro criado")
        self.titulo = t
        self.autor = a
        self.paginas = p
    def __str__(self):
        return f'Titulo: {self.titulo} | Autor: {self.autor} | Paginas: {self.paginas}'
    def __len__(self):
        return self.paginas
    def len(self):
        return f'Paginas: {self.paginas}'


livro1 = Livros("As 32 Leis do Poder", "Robert Green", 300)

print(livro1)
# Quando se usa a funcao print em qualquer situacao, o metodo __str__ o qual ja vem na linguagem python, é executado.
# Neste caso, livro1 representa o self, entao o que esta dentro do metodo __str__ (da classe Livros) é retornado
str(livro1)

print(len(livro1))
print(livro1.len())

del livro1.paginas
print(hasattr(livro1, "paginas"))
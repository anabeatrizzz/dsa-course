# A herança nos ajuda a economizar linhas de codigo, uma vez que temos uma classe com varios metodos, apenas temos que criar outra classe que recebe esta que possui varios metodos como parametro.

class Animal():
    def __init__(self):
        print("Animal criado")
    def identificar(self):
        print("Animal")
    def comer(self):
        print("Comendo")


# Esta classe terá seus proprios metodos mas tambem pode herdar metodos da classe Animal.
class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Objeto cachorro criado")
    # Quando um objeto da classe Cachorro for criado, as funcoes construtoras das classes Cachorro e Animal.
    def identificar(self):
        print("Cachorro")
    def latir(self):
        print("Au! Au!")


lilica = Cachorro()
lilica.identificar()
# Como há duas funcoes identificar, a que está na classe Cachorro terá prioridade pois, o objeto lilica pertence a essa classe.
lilica.comer()
lilica.latir()
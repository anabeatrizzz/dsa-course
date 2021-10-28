class Circulos:
    pi = 3.14
    def __init__(self, r=5):
        self.raio = r
    def area(self):
        return (self.raio * self.raio) * Circulos.pi
    def setRaio(self, novo):
        self.raio = novo
    def getRaio(self):
        return self.raio


circulo1 = Circulos()
circulo1.getRaio()

circulo2 = Circulos(7)
circulo2.getRaio()

print(f'O raio é {circulo1.getRaio()}')

print(f'A area é igual a {circulo1.area()}')

circulo1.setRaio(3)
print(f'O valor do novo raio é {circulo1.getRaio()}')
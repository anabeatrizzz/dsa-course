class Estudantes:
    def __init__(self, n, i, no):
        self.nome = n
        self.idade = i
        self.nota = no


estudante1 = Estudantes("Ana", 18, 10.00)
print(f'{estudante1.nome}\n{estudante1.idade}\n{estudante1.nota}')

class Funcionarios:
    def __init__(self, n, s):
        self.nome = n
        self.salario = s
    def listar(self):
        print(f'O(A) funcionario(a) {self.nome} tem o salario de R${self.salario}')


funcionario1 = Funcionarios("Ana", 20000)
funcionario1.listar()

hasattr(funcionario1, "nome")
# O objeto funcionario1 tem atributo 'nome'?

hasattr(funcionario1, "salario")
# O objeto funcionario1 tem atributo 'salario'?

setattr(funcionario1, "salario", 30000)
# Atribua o valor 30000 ao atributo salario do objeto funcionario1 

getattr(funcionario1, "salario")
# Mostre o valor do atributo salario do objeto funcionario1 

delattr(funcionario1, "salario")
# Apague o atributo salario do objeto funcionario1 
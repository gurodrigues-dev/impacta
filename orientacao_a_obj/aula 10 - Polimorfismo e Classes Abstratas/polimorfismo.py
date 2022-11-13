class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f"O {self.nomeclasse} {self.nome} está falando...")

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")


class Aluno(Pessoa):
    pass


class Funcionario(Pessoa):
    pass


a1 = Aluno("Gustavo", 18)
a1.exibir_dados()
a1.falar()

f1 = Funcionario("Paulo", 21)
f1.exibir_dados()
f1.falar()

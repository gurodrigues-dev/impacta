from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def exibir_alunos(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade, turma, escola):
        super().__init__(nome, idade)

    def exibir_alunos(self):
        print(f"Aluno: {self.nome}")

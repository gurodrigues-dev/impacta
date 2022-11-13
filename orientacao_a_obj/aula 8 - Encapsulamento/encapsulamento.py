class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__horas_trabalhadas = 0
        self.__salario = 0

    def registra_hora_trabalhada(self):
        self.horas_trabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada

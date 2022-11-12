class Funcionario():
    def __init__(self, nome: str, salario: int):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percentual: int):
        percentual = ((self.salario * percentual) / 100)
        self.salario += percentual


nome = input("Nome: ")
salario = int(input("Salário: "))
funcionario1 = Funcionario(nome, salario)

percentual = int(input("Em quanto você quer aumentar seu salário: "))
funcionario1.aumentar_salario(percentual)

print(f"O salário de {funcionario1.nome} agora é de: {funcionario1.salario}")

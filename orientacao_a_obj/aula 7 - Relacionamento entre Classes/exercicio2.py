class Endereco():
    def __init__(self, rua: str, numero: int, cep: int):
        self.rua = rua
        self.numero = numero
        self.cep = cep

    def exibir_dados(self):
        print(f"Rua: {self.rua}")
        print(f"Número: {self.numero}")
        print(f"CEP: {self.cep}")


class Pessoa():
    def __init__(self, nome: str, sobrenome: str, idade: int, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.endereco = endereco

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Sobrenome: {self.sobrenome}")
        print(f"Nome completo: {self.nome} {self.sobrenome}")
        print(f"Idade: {self.idade}")
        self.endereco.exibir_dados()


address = Endereco("Rua Itamerendiba", 32, 999)
gustavo = Pessoa("Gustavo", "Rodrigues", 18, address)
gustavo.exibir_dados()

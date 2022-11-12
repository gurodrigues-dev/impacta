class Cachorro():

    # atributos

    def __init__(self):
        self.nome = None
        self.idade = None

    # métodos

    def latir(self):
        print(f"O cachorro {self.nome} latiu")

    def andar(self, distancia):
        print(f"O cachorro andou {distancia} metros")

    def comer(self):
        print(f"O cachorro {self.nome} comeu")


dog = Cachorro()

dog.andar(2)
dog.nome = "Rex"
dog.idade = 4
print(f"O cachorro de nome {dog.nome} possui a idade de {dog.idade}")
dog.comer()
dog.latir()

meu_cachorro = Cachorro()
meu_cachorro.nome = "Snoopy"
meu_cachorro.idade = 2
print(
    f"O cachorro de nome {meu_cachorro.nome} possui a idade de {meu_cachorro.idade}")
meu_cachorro.andar(5)
meu_cachorro.comer()
meu_cachorro.latir


class Gato():

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def andar(self):
        print(f"O gato {self.nome} andou")

    def comer(self, comida):
        print(f"O gato {self.nome} comeu {comida}")

    def miar(self):
        print(f"O gato {self.nome} miou")


tom = Gato("Tom", 10)
tom.andar()
tom.comer("Peixe")
tom.miar()

print(tom.nome)
print(tom.idade)

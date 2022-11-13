class Aluno():

    def __init__(self, ra, nome, turma):
        self.ra = ra
        self.nome = nome
        self.turma = turma
        self.notas = []
        self.media = None

    def inserir_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        self.media = (sum(self.notas) / len(self.notas))


ra = input("RA: ")
nome = input("Nome: ")
turma = input("Turma: ")

aluno1 = Aluno(ra, nome, turma)

count = int(input("Quantas provas você teve: "))

for i in range(0, count, 1):
    nota = int(input(f"Digite sua nota na prova: "))
    aluno1.inserir_nota(nota)

aluno1.calcular_media()
print(f"O {aluno1.nome} fechou o semestre com {aluno1.media}")

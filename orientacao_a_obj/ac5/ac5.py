# ATIVIDADE CONTÍNUA 05

# NOMES DOS ALUNOS: (MÁXIMO 6):
# Aluno 1 : Gustavo Rodrigues Lima

# IMPORTAR MÓDULOS
from sqlalchemy import create_engine, Column, Integer, String, Float 
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# CONFIGURAR CONEXÃO COM BANCO DE DADOS SQLITE
engine = create_engine("sqlite:///C:\\Users\\gulima\\Desktop\\faculdade\\poo\\database.db")
connection = engine.connect()

def exibelinhas():
    print("-"*30)

# INICIAR SESSÃO COM BANCO DE DADOS
session = Session()

# INSTANCIAR CLASSE BASE DO SQLALCHEMY
Base = declarative_base(engine)

# Cria a tabela FILME no banco de dados
connection.execute("""CREATE TABLE IF NOT EXISTS FILME(
                        ID INTEGER PRIMARY KEY,
                        TITULO VARCHAR(255),
                        ANO INT,
                        DURACAO INT,
                        PAIS VARCHAR(255),
                        DIRETOR VARCHAR(255),
                        AVALIACAO FLOAT)""")

# Implementar classe Filme e realizar o mapeamento da tabela
class Filmes(Base):
    __tablename__ = 'FILME'
    id        = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo    = Column('TITULO', String(255))
    ano       = Column('ANO', Integer)
    duracao   = Column('DURACAO', Integer)
    pais      = Column('PAIS',String(50))
    diretor   = Column('DIRETOR',String(75))
    avaliacao = Column('AVALIACAO',Integer)

    def __init__(self, titulo, ano, duracao, pais, diretor, avaliacao):
        self.titulo    = titulo
        self.ano       = ano
        self.duracao   = duracao
        self.pais      = pais
        self.diretor   = diretor
        self.avaliacao = avaliacao

# Importar filmes do arquivo de texto movies.txt e inserir no banco de dados
lista_filmes = []
with open('filmes.txt', 'r') as file:
    rows = file.readlines()

    for row in rows:
        row  = row.split(";")
        func = Filmes(row[0], int(row[1]), int(row[2]), row[3], row[4], int(row[5]))
        lista_filmes.append(func)

session.add_all(lista_filmes)
session.commit()

# Consultar todos os filmes e ordenar pelo título
exibelinhas()
resultado = session.query(Filmes).order_by(Filmes.titulo)
for obj in resultado:
    print(obj.id, obj.titulo, obj.ano, obj.duracao, obj.pais, obj.diretor, obj.avaliacao)

# Consultar filmes do ano de 2020 e ordenar pelo título
exibelinhas()
resultado = session.query(Filmes).filter(Filmes.ano == 2020).order_by(Filmes.titulo)
for obj in resultado:
    print(obj.id, obj.titulo, obj.ano, obj.duracao, obj.pais, obj.diretor, obj.avaliacao)

# Consultar filmes de 2019 com avaliação superior a 80 e ordenar pelo título
exibelinhas()
resultado = session.query(Filmes).filter(Filmes.avaliacao == 80).order_by(Filmes.titulo)
for obj in resultado:
    print(obj.id, obj.titulo, obj.ano, obj.duracao, obj.pais, obj.diretor, obj.avaliacao)

# Excluir todos os filmes do ano de 2020
resultado = session.query(Filmes).filter(Filmes.ano == 2020).delete()
session.commit()

# Exportar filmes para um arquivo de texto, ordenados pelo título e no formato:
# título;ano;duracao;país;diretor;avaliacao
resultado = session.query(Filmes).order_by(Filmes.titulo)
for obj in resultado:
    f = open("new_filmes.txt", "a")
    f.write(obj.titulo, obj.ano, obj.duracao, obj.pais, obj.diretor, obj.avaliacao)
    f.close()
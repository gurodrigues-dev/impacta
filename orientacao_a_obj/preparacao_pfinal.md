# Filas e Pilhas - AULA 11
> O conceito de filas e pilhas é bem simples, um é contrário do outro.

### Filas
> Filas são simples, o primeiro que chega a uma fila é sempre o primeiro a ser atendido, no caso da programação a sair. Sempre por ordem de chegada.

- Segue um exemplo em python:
    ```python
    def enfileirar(x):
    	# neste caso estariamos adicionando um numero a fila
    	fila.append(x)

    def desinfileirar():
    	fila.remove(fila[0])

    # criando a fila
    fila = []

    enfileirar(1)
    enfileirar(2)
    enfileirar(3)

    print(fila)
    # Retorno -> [1,2,3]

    desinfileirar()
    # agora a fila está da seguinte maneira [2,3]

    desinfileirar()
    # agora [3]
    ```

### Pilhas
> Ao contrário de Filas, você sempre tira o que acabou de entrar então imagine uma pilha de livros, você precisa tirar os livros dali, o que você vai fazer então, tirar o último que colocou. 

- Segue um exemplo em python:
    ```python
    def empilhar(x):
    	# adicionando a pilha
	pilha.append(x)

    def desimpilhar():
	pilha.pop()

    pilha = []

    empilhar(1)
    empilhar(2)
    empilhar(3)

    print(pilha)
    # O retorno seria o seguinte: [1, 2, 3]

    desimpilhar()
    # agora [1,2]

    desimpilhar
    # agora [1]
    ```
# Orientação a Objetos

## Lembretes

- Para usar classe no Python sempre utilize a função de POO. class <Nome da Classe>(atributo, atributos)

- O que é um construtor?
     R: Onde você inicia os atributos de uma classe, com o famoso init.

     ```python
     def __init__(self, nome, idade):
        ...
     ```

## Relacionamento entre classes - AULA 7
> Quando uma classe necessita de atributos de outra classe.

- Segue exemplo em python:
     ```python
     class Endereco():
     	def __init__(self, rua, numero, cep):
	     self.rua = rua
	     self.numero = numero
	     self.cep = cep
	
	def exibir_endereco(self):
	print(f"Rua: {self.rua}")
	print(f"Numero: {self.numero}")
	print(f"CEP: {self.cep}")

     class Pessoa():
     	def __init__(self, nome, sobrenome, idade, endereco):
	     self.nome = nome
	     self.sobrenome = sobrenome
	     self.idade = idade
	     self.endereco = endereco

	def exibir_dados(self):
	     print(f"NOme: {self.nome}")
	     print(f"Sobrenome: {self.sobrenome}")
	     print(f"Idade: {self.idade}")
	     self.endereco.exibir_endereco()

     address = Endereco("Rua Impacta" 2, 999)
     gustavo = Pessoa("Gustavo", "Rodrigues", 18, address)
     gustavo.exibir_dados()

     # Retorno esperado "Gustavo Rodrigues 18 Rua Impacta 2 999"

     ```

## Encapsulamento - AULA 8
> Simples. O conceito de encapsulamento é quando uma classe não deve ser usada de forma pública, como assim?

Suponha que existe uma classe para cada individuo e um dos métodos lida com o dinheiro do usuário, você quer que isso seja exibido publicamente? Não. Então esse metodo ou classe precisa ser privado. No Python isso não funciona como nas outras linguagens.

Geralmente nas outras linguagens utilizamos o private <Class> ou private <método>.

Mas no Python, não funciona assim, você deve utilizar dois underscores para determinar essa classe privada.

- Segue o exemplo no Python:
> No exemplo abaixo horas trabalhas e salario, serão privados.
    ```python
    class Funcionario():
        def __init__(self, nome, cargo, valor_hora_trabalhada):
	     self.nome = nome
	     self.cargo = cargo
	     self.valor_hora_trabalhada = valor_hora_trabalhada
	     self.__horas_trabalhadas = 0
	     self.__salario = 0

	def registra_hora_trabalhada(self):
	     self.__horas_trabalhadas += 1

	def calcula_salario(self):
	     self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada

    ```

## Herança - AULA 9
Quando uma classe filha (subclasse) herda atributos de uma classe mae (superclasse)

- Segue código no python:
    ```python
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
    ```


## Polimorfismo - AULA 10
Quando uma sublcasse, utiliza metodos de uma classe maior

    Exemplo:
    ```python
    class Pessoa():
	def __init__(self, nome, idade):
	    self.nome = nome
	    self.idade = idade
	    self.nomeclasse = self.__class__.__name__

	def falar(self):
	    print(f"{self.nome) da classe {self.nomeclasse} da idade {self.idade} está falando.")

    class Aluno(Pessoa):
    	pass

    class Funcionario(Pessoa):
    	pass

    a1 = Aluno("Gustavo", 18)
    a1.falar()

    # Retorno 
    "Gustavo da classe Aluno da idade 18 está falando."
    ```

## Classe Abstrata - AULA 11
A classe abstrata sempre tem a importação da lib ABC, conforme o exemplo abaixo:
    ```python
    import abc

    # Caso precise de métodos abstratos, será necessário a importação dos metodos abstratos 

    from abc import ABC, abstractmethod
    ```

    Criando uma classe abstrata e em seguida usando um método abstrato
    ```python
    from abc import ABC, abstractmethod

    class Pessoa(ABC):
    	def __init__(self, nome, idade):
	self.nome = nome
	self.idade = idade

    @abstractmethod
    def exibir_alunos(self)
  	pass
    ```

## Possíveis questões

- Quais são os 4 pilares da Orientação a Objetos.
    R: Polimorfismo, Herança, Encapsulamento e Classes Abstratas.

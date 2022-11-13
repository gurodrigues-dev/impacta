def empilhar(x):
    pilha.append(x)
    return


def desimpilhar():
    pilha.pop()
    return


pilha = []

empilhar(100)
empilhar(200)
empilhar(300)

print(pilha)

desimpilhar()

print(pilha)

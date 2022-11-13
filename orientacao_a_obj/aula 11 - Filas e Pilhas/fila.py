def enfileirar(x):
    fila.append(x)


def desinfileirar():
    fila.remove(fila[0])


fila = []

enfileirar(100)
enfileirar(200)
enfileirar(300)

print(fila)

desinfileirar()
desinfileirar()

print(fila)

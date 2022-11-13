cdc = input().split()

if (cdc != []):
    for i in range(len(cdc)):
        cdc[i] = int(cdc[i])

def add(lista, item):
    lista.append(item)

def remover(lista, item):
    if (item in lista):
        lista.remove(item)
    else:
        print(f'código {item} não encontrado')

def mostrar(lista):
    lista.sort()

    for i in range(len(lista)):
        if (i < len(lista) - 1):
            print(lista[i], end=' ')
        else:
            print(lista[i])

command = input().split()

while command[0] != 'encerrar':
    if (command[0] == 'adicionar'):
        add(cdc, int(command[1]))
    elif (command[0] == 'remover'):
        remover(cdc, int(command[1]))
    else:
        mostrar(cdc)

    command = input().split()

mostrar(cdc)
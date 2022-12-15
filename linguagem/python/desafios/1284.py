x = int(input())

def on():
    notas = []

    for _ in range(x):
        notas.append(float(input()))

    return notas

def onf(no, nn):
    qtd_na = 0

    for i in range(len(no)):
        if (nn[i] == 10 and no[i] < 10):
            nn[i] = min(no[i] + 2, 10)
            qtd_na += 1
        else:
            nn[i] = no[i]

    return qtd_na

def ena(no, nf, qtd_na):
    print(f'NOTAS ALTERADAS: {qtd_na}')
    for i in range(x):
        na = ('*' if no[i] != nf[i] else '-')
        print(f'{na}({i+1:03}) original: {no[i]:05.2f} | final: {nf[i]:05.2f}')

if (1 <= x <= 999):
    no = on()
    nn = on()
    qtd_na = onf(no, nn)
    ena(no, nn, qtd_na)
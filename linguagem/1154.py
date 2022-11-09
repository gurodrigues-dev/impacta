lista = []

condicao = True 

while condicao is True:
    x = int(input())
    if x > 0:
        lista.append(x)
    else:
        media = sum(lista) / len(lista)
        condicao = False

print(f"{media:.2f}")
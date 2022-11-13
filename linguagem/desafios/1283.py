lista = []

x = int(input())

while x > 0:
    lista.append(x)
    x = int(input())

res = sum(lista) / len(lista)
print(f'MEDIA: {res:.2f}')

for i in lista:
    if i < res:
        print(i)
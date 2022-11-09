lista = []

x = int(input())
newnumber = 1
res = 1

for i in range(1, x+1):
    lista.append(newnumber)
    newnumber += 1

for i in lista:
    res *= i

print(res)
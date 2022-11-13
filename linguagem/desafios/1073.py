numeros = []
pares = [] 

N = int(input())

acumulador = 1

if N > 5 and N < 2000:
    for i in range(1, N+1):
        numeros.append(acumulador)
        acumulador = acumulador + 1

for i in numeros:
    if i % 2 == 0:
        pares.append(i)

for par in pares:
    x = par ** 2
    print (f'{par}^2 = {x}')
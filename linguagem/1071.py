impares = []

X = int(input(''))
Y = int(input(''))

if X > Y:
    valor_max = X
    valor_min = Y
else: 
    valor_max = Y
    valor_min = X

valor_min = valor_min + 1

lista = [] 

for i in range(valor_min, valor_max, 1):
    lista.append(i)

for i in lista:
    if i % 2 == 1:
        impares.append(i)

res = sum(impares)       
    
print(res)
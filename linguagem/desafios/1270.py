lista = []

x = int(input())
y = int(input())

count = 0

if x > y:
    print('Nenhuma tabuada no intervalo!')
else:
    for i in range(x, y+1):
        lista.append(i)
        for mult in lista:
            while count < 10:
                count += 1
                print(f'{i} x {count} = {i * count}')
        print('-'*10)
        count = 0
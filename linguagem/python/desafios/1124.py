number = int(input())
acumulador = 0
sucessor = 0
ante = 0
if number % 2 == 0:
    acumulador = number + 2
    ante = number - 1
    print (f'{ante} {acumulador}')
else:
    acumulador = number - 2
    sucessor = number + 1
    print (f'{acumulador} {sucessor}')
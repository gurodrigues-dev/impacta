x = int(input())
y = int(input())
pagamento = 0
antes = 0
depois = 0

while x > 0:
    pagamento += 1
    print(f'pagamento: {pagamento}')

    antes = x 
    print(f'antes = {antes}')

    depois = x = x - y
    if depois < 0:
        print(f'depois = 0')
    else:
        print(f'depois = {depois}')

    print('-' *  5)
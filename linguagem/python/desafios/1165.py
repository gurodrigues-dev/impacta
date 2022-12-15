x = 0
y = 0
while y > -1.0:
    y = float(input())
    if y == -1.0:
        x += 1
    x += y
    z = x * 2.50
print('VC$ {:.2f}'.format(x))
print('R$ {:.2f}'.format(z))
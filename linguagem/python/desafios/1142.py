x = int(input())

if x >= 0 and x <= 10:
    for i in (range(1, 11, 1)):
        print(f'{x} x {i} = {x*i}')
def maindiagonal(x: list, y: list, z: list):
    a11 = x[0]
    b22 = y[1]
    c33 = z[2]
    return a11 + b22 + c33

def secondiagonal(x: list, y: list, z: list):
    a13= x[2]
    b22 = y[1]
    c31 = z[0]
    return a13 + b22 + c31

try: 

    number = int(input())
    array = list(map(int, input().rstrip().split(" ")))
    array_1 = list(map(int, input().rstrip().split(" ")))
    array_2 = list(map(int, input().rstrip().split(" ")))

    main = maindiagonal(array, array_1, array_2)
    second = secondiagonal(array, array_1, array_2)
    result_matriz = second - main
    print(result_matriz)

except Exception as err:
    print(err)


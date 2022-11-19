try:
    number = int(input())
    matriz = []
    count_primaria = -1
    count_secundaria = -1
    primaria = 0
    secundaria = 0
    
    for i in range(number):
        array = list(map(int, input().rstrip().split(" ")))
        matriz.append(array)

    # calculo da matriz principal 
    for item in matriz:
        count_primaria += 1
        primaria += item[count_primaria]

    # calculo da matriz secundaria
    matriz.reverse()
    
    for item in matriz:
        count_secundaria += 1
        secundaria += item[count_secundaria]

    if primaria > secundaria:
        resultado = primaria - secundaria
        print(resultado)
    else:
        resultado = secundaria - primaria
        print(resultado)
    
except Exception as err:

    print(err)
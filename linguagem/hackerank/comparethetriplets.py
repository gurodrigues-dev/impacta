try:

    alice = 0
    bob = 0

    a1, a2, a3 = input().split(" ")
    a1 = int(a1)
    a2 = int(a2)
    a3 = int(a3)
    
    b1, b2, b3 = input().split(" ")
    b1 = int(b1)
    b2 = int(b2)
    b3 = int(b3)

    matriz_a = [a1, a2, a3]
    matriz_b = [b1, b2, b3]

    for number in range(3):
        if matriz_a[number] > matriz_b[number]:
            alice += 1
        elif matriz_a[number] == matriz_b[number]:
            pass
        else:
            bob += 1

    print(f"{alice} {bob}")

except Exception as err:
    print(err)
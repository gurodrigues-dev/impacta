N1, N2, N3, N4 = input().split(" ")

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1))/10

print(f'Media: {media:.1f}')

if media >= 7.0:
    print("Aluno aprovado.")
elif media <= 4.9:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")

    N5 = float(input())
    newmedia = ((media + N5) / 2)

    print(f'Nota do exame: {N5:.1f}')

    if newmedia >= 5:
        print("Aluno aprovado.")

        print(f'Media final: {newmedia:.1f}')
        
    elif newmedia <= 4.9:
        print("Aluno reprovado.")

        print(f'Media final: {newmedia:.1f}')
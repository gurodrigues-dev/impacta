x = int(input(""))

count_de_dias = 0
dias = []

for i in range(0, x):
    count_de_dias += 1
    dias.append(count_de_dias)

feedbacks = []

for i in dias:
    k = int(input(f""))
    for i in range(0, k):
        y = int(input(""))
        feedbacks.append(y)

for i in feedbacks:
    if i == 1:
        print("Rolien")
    if i == 2:
        print("Naej")
    if i == 3:
        print("Elehcim")
    if i == 4:
        print("Odranoel")
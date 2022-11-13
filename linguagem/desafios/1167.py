x = int(input(""))
y = int(input(""))
count = 0

for n in range(x, y + 1):
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        print(n)
        count += 1
                
print(f"bissextos: {count}")
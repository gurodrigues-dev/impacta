numbers = list()
for i in range(100):
    numbers.append(int(input()))

print(max(numbers))
print(numbers.index(max(numbers))+1)
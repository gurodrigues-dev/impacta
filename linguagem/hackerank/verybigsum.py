try:
    count = 0
    
    number = int(input())
    array = list(map(int, input().rstrip().split(" ")))
    
    for item in array:
        count += item
        
    print(count)

except Exception as err:
    print(err)

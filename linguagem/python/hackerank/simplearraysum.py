try:
    number = int(input())   
    array = list(map(int, input().rstrip().split(" ")))
    print(sum(array))
except Exception as err:
    print(err)


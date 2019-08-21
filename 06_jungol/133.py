n = int(input())
numbers = list(map(int, input().split()))
result = sum(numbers)/len(numbers)
print('%.2f'%result)
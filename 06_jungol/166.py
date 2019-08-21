arr1 = [list(map(int, input().split())) for _ in range(2)]
arr2 = [list(map(int, input().split())) for _ in range(2)]

print('first array')
print('second array')
for i in range(2):
    for j in range(3):
        print(arr1[i][j] * arr2[i][j], end=' ')
    print()
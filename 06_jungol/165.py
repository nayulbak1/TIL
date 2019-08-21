arr = [[0] * 5 for _ in range(5)]
arr[0][0] = arr[0][2] = arr[0][4] = 1

for i in range(1, 5):
    for j in range(5):
        if j != 0:
            arr[i][j] += arr[i - 1][j - 1]
        if j != 4:
            arr[i][j] += arr[i - 1][j + 1]

for i in range(5):
    for j in range(5):
        print(arr[i][j],end=' ')
    print()

arr = [3, 6, -2, 7, -3, 1, -5, -1, 5, 4]
n = len(arr) # 원소의 개수: 10
subset = 10
for i in range(1, 1 << n):    # i는 부분집합을 표현
    sum = 0
    for j in range(n + 1):
        if i & (1 << j):    # arr[j]를 포함하는지 여부
            sum += arr[j]
    if sum == 0:
        for j in range(n + 1):
            if i & (1 << j):  # arr[j]를 포함하는지 여부
                print(arr[j], end=' ')
        print()
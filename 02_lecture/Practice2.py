arr = [64, 25, 10, 22, 11]
N = len(arr)
# 최솟값 위치 [0, n-1]

for i in range(0, N-1):
    minIdx = i
    for j in range(i+1, N):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]
print(arr)
#버블 정렬

#1
arr = [55, 7, 78, 12, 42]
n = len(arr)
for j in range(n-1, 0, -1):
    for i in range(j):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)

#2
min = arr[0]
for i in range(1, len(arr)):
    if arr[i] < min:
        min = arr[i]
print(min)

#3
for j in range(len(arr)-1):
    min = j
    for i in range(j+1, len(arr)):
        if arr[i] < arr[min]:
            min = i
    arr[j], arr[min] = arr[min], arr[j]

#Counting
data = [0, 3, 1, 3, 1, 2, 4, 1]

#1
counts = [0] * 5
for value in data:
    counts[value] += 1
print(counts)

#2
sorted = []
for i in range(len(counts)):
    for j in range(counts[i]):
        sorted.append(i)
print(sorted)

#3
for i in ragne(len(counts)):
    counts[i] = counts[i-1] + counts[i]

# baby-gin game
# 결정 문제
# 최적화 문제
# 최대 혹은 최소가 되는 경우를 찾는 문제

data = 'ABC'

n = len(data)
for i in range(n):
        for j in range(n):
                if i == j: continue:
                for k in range(n):
                        if i == k or j == k: continue:
                        print(data[i], data[j], data[k])
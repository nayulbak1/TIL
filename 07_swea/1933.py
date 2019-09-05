N = int(input())
for i in range(1, N+1):
    if N % int(i) == 0:
        print(i, end=' ')
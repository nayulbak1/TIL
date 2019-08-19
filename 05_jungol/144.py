n = int(input())
for i in range(1, n+1, +2):
    if i <= n:
        print(' '*(n-i) + i*'*')

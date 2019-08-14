n = int(input())
for i in range(1, n+1):
    if i <= n:
        print(i*'*')
for j in range(n, n*2):
    if j > n:
        print((n*2-j)*'*')
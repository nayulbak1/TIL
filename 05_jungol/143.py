n = int(input())
for i in range(n, 0, -2):
    if i <= n:
        print(i*'*')
for j in range(n, n*2+1, +2):
    if j > n+1:
        print((j-n)*'*')
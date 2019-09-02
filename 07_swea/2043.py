import sys; sys.stdin=open("2043.txt", "r")

P, K = map(int, input().split())
cnt = 0
for i in range(1, P-K+2):
    cnt = i
print(cnt)
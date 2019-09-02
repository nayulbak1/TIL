import sys; sys.stdin=open('2072.txt', 'r')

T = int(input())
for i in range(1, T+1):
    N = list(map(int, input().split()))
    cnt = 0
    for j in N:
        if j %2 == 1:
            cnt += j
    print('#{} {}'.format(i, cnt))  
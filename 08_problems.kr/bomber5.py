import sys; sys.stdin=open('bomber5_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    S = 0
    for i in range(M):
        r, c = map(int, input().split())
        for i in range(N):
            S += arr[r][i]
            arr[r][i] = 0
            S += arr[i][c]
            arr[i][c] = 0

    print('#{} {}'.format(tc, S))
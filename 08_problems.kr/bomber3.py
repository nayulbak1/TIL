import sys; sys.stdin=open('bomber3_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = a = b = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            S = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    S += arr[x][y]

            if ans < S:
                    ans, a, b = S, i, j

print('#{} {} {} {}'.format(tc, a, b, ans))
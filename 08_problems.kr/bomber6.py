import sys; sys.stdin=open('bomber6_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 지도 크기, M은 폭탄 수
    arr = [list(map(int, input().split())) for _ in range(N)]

    S = 0
    for _ in range(M): # 폭탄 수만큼 이하를 반복
        x, y, r = map(int, input().split()) # x는 폭탄이 투하되는 행, y는 그 열, r은 폭발 범위
        S += arr[x][y]
        arr[x][y] = 0

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # 우, 좌, 하, 상
            a, b = x, y
            for i in range(r): # 폭발 범위만큼 이하를 반복
                a, b = a + dx, b + dy
                if a < 0 or b < 0 or a >= N or b >= N: break
                S += arr[a][b]
                arr[a][b] = 0

    print('#{} {}'.format(tc, S))
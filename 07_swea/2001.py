import sys; sys.stdin=open('2001.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    maximum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            shocked_area = 0
            for x in range(M):
                for y in range(M):
                    shocked_area += flies[i+x][j+y]
            if shocked_area > maximum:
                maximum = shocked_area

    print('#{} {}'.format(tc + 1, maximum))
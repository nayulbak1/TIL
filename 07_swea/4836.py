import sys; sys.stdin=open('4836.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    red_square = []
    blue_square = []
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if color == 1:
                    red_square.append((r, c))
                if color == 2:
                    blue_square.append((r, c))

    result = []
    if len(red_square) > len(blue_square):
        for i in blue_square:
            if i in red_square:
                result.append(i)
    if len(blue_square) > len(red_square):
        for i in red_square:
            if i in blue_square:
                result.append(i)

    print('#{} {}'.format(tc, len(result)))

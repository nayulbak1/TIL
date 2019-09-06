import sys; sys.stdin=open('1945.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while N > 1:
        if N % 2 == 0:
            a += 1
            N = int(N / 2)
        if N % 3 == 0:
            b += 1
            N = int(N / 3)
        if N % 5 == 0:
            c += 1
            N = int(N / 5)
        if N % 7 == 0:
            d += 1
            N = int(N / 7)
        if N % 11 == 0:
            e += 1
            N = int(N / 11)
    print("#{} {} {} {} {} {}".format(tc+1, a, b, c, d, e))
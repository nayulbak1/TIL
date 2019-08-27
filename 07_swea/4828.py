import sys; sys.stdin=open('4828.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    minimum = ai[0]
    maximum = ai[0]
    for a in ai[1:]:
        if minimum > a:
            minimum = a
    for b in ai[1:]:
        if maximum < b:
            maximum = b
    result = maximum - minimum
    print('#{} {}'.format(tc, result))
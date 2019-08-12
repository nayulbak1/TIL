x = int(input())
for i in range(1, x+1):
    a, b = map(int, input().split())
    print('Case #%d: %d' % (i, a+b))
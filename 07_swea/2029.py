import sys; sys.stdin=open('2029.txt','r')

T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    x = a // b
    y = a % b
    print('#{} {} {}'.format(tc+1, x, y))
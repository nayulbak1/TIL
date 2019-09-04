import sys; sys.stdin=open('2070.txt', 'r')
T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    result = '>' or '<' or '='
    if a > b:
        result = '>'
    elif a < b:
        result = '<'
    elif a == b:
        result = '='
    print('#{} {}'.format(tc+1, result))
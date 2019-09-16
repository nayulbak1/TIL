import sys; sys.stdin=open('1966.txt', 'r')

for tc in range(int(input())):
    N = int(input())
    numbers = sorted(list(map(int, input().split())))
    print('#{}'.format(tc+1), *numbers)
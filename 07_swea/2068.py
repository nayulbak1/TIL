import sys; sys.stdin=open('2068.txt', 'r')

T = int(input())
for tc in range(T):
    N = list(map(int, input().split()))
    print('#{} {}'.format(tc+1, max(N)))
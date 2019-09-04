import sys; sys.stdin=open('2071.txt', 'r')

T = int(input())
for tc in range(T):
    N = list(map(int, input().split()))
    sum = 0
    for i in N:
        sum += i
        average = sum/10
    print('#{} {}'.format(tc+1, round(average)))
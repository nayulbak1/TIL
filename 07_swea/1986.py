import sys; sys.stdin=open('1986.txt', 'r')

for tc in range(int(input())):
    N = int(input())
    odd_sum = int()
    for i in range(1, N+1):
        if i%2 == 0:
            odd_sum -= i
        else:
            odd_sum += i

    print('#{} {}'.format(tc+1, odd_sum))
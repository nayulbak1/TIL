N = int(input())
if 1 <= N <= 9:
    for j in range(1, 10):
        print('{} * {} = {}'.format(N, j, N * j))
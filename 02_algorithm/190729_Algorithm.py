import sys
sys.stdin = open("input.txt", "r")

for N in range(1, 11):
    n = int(input())
    num = list(map(int, input().split()))

    result = 0
    for i in range(2, n-2):
        MAX = max(num[i-2], num[i-1], num[i+1], num[i+2])
        if MAX < num[i]:
                result += num[i] - MAX
    print('#%d %d' % (N, result))
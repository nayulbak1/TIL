import sys
sys.stdin = open("sum.txt", "r")

#1
 
# testcase = int(input())
# box = []
# for sample in range(testcase):
#     for i in range(100):
#         item = list(map(int, input().split()))
#         box.append(item)

for test_case in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    MAX = 0
    dsum1 = dsum2 = 0
    for i in range(100):
        rsum = csum = 0
        dsum1 += arr[i][i]
        dsum2 += arr[i][99 - i]
        for j in range(100):
            rsum += arr[i][j]
            csum += arr[j][i]
        MAX = max(MAX, rsum, csum)
    print('#%d %d' % (test_case, MAX))
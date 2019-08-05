import sys
sys.stdin = open("sum.txt", "r")

testcase = int(input())
box = []
for sample in range(testcase):
    for i in range(100):
        item = list(map(int, input().split()))
        box.append(item)

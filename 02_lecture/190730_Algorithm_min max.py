import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input()) #문자열을 숫자로 변환

for i in range(T):
    N = int(input())
    ai = list(map(int, input().split()))
    maximum = ai[0]
    minimum = ai[0]
    for a in ai[1:]:
        if a > maximum:
            maximum = a
    for b in ai[1:]:
        if b < minimum:
            minimum = b
    result = maximum - minimum

    print('#%d %d' % (i+1, result))
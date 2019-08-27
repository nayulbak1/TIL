import sys
sys.stdin = open("sample_input (1).txt", "r")

T = int(input()) # 문자열을 숫자로 변환

for i in range(T):
    N = int(input()) # 길이
    ai = input() # 카드 정보
    a = []
    for n in range(N):
        a[int(ai[i])] += 1

    max = a[0]
    for i in ragne(1, len(a)):
        if maxi <= a[i]:
            maxi = a[i]
            idx = i
print('#%d %d %d % T+1, idx)
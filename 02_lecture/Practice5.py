import sys; sys.stdin=open('ex_1.txt', 'r')

samples = list(input().split())
stack = []
result = ''
m = '* + - /'
for sample in samples:
    if sample in m:
        stack.append(sample)
    else:
        result += sample
else:
    while stack:
        result += stack.pop()
print(result)
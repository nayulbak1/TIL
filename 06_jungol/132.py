n = int(input())
a = []
for i in range(1, n+1):
    if i % 5 == 0:
        a.append(i)
print(sum(a))
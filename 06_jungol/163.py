arr = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]

S = 0
for row in arr:
    for val in row:
        print('{} '.format(val), end='')
        S += val
    print()
print(S)
for x in range(65, 200, 1):
    print('code point', x, '=', chr(x))

alphabet = input()
for i in alphabet:
    N = ord(i) - 64
    print(N, end=' ')
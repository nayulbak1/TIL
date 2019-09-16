import sys; sys.stdin=open('2007.txt', 'r')

for tc in range(int(input())):
    random = input()
    word = 0
    for i in range(len(random)):
        if random[:i] == random[i:i*2] and len(random[:i]) != 0:
            word = i
            break
    print('#{} {}'.format(tc+1, word))
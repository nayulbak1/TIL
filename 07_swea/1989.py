import sys; sys.stdin=open('1989.txt', 'r')

for tc in range(int(input())):
    word = str(input())
    if word[0] == word[-1] and word[1] == word[-2]:
        ans = 1
    else:
        ans = 0
    print('#{} {}'.format(tc+1, ans))
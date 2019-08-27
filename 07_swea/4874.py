import sys; sys.stdin=open('forth.txt', 'r')

T = int(input())
for sample in range(T):
    info = list(input().split())
    math = '+ - * /'
    s = []
    for i in info:
        if i not in math and i != '.':
            i = int(i)
            s.append(i)
        else:
            if len(s) > 1:
                b = s.pop()
                a = s.pop()
                if i == '+':
                    s.append(a+b)
                elif i == '-':
                    s.append(a-b)
                elif i == '*':
                    s.append(a*b)
                elif i == '/':
                    s.append(a//b)
                else:
                    print('#{} error'.format(sample+1))
                    break
            else:
                print('#{} {}'.format(sample+1, s[0]))
import sys; sys.stdin=open("1936.txt","r")

def winner(A, B):
    if A == 1 and  B == 2 :
        print('B')
    if A == 2 and  B == 3 :
        print('B')
    if A == 3 and  B == 1 :
        print('B')
    if A == 2 and  B == 1 :
        print('A')
    if A == 3 and  B == 2 :
        print('A')
    if A == 1 and  B == 3 :
        print('A')
        
A, B = map(int, input().split())

winner(A, B)
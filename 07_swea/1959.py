import sys; sys.stdin=open('1959.txt', 'r')

for tc in range(int(input())):
    A, B = map(int, input().split() )
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arrsum = []
    if A>B:
        for j in range(A-B+1):
            arrsum += [sum([arr1[z+j]*arr2[z] for z in range(B)])]
    else:
        for j in range(B-A+1):
            arrsum += [sum([arr1[z]*arr2[z+j] for z in range(A)])]
    print(f'#{tc+1} {max(arrsum)}')
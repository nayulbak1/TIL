H, M = map(int, input().split())
0<=H<=23, 0<=M<=59
if H == 0 and 0<=M<45:
    print(23, M-45+60)
elif 45<=M<=59:
    print(H, M-45)
elif 0<=M<45:
    print(H-1, M-45+60)
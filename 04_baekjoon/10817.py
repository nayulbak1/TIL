A, B, C = map(int, input().split())
if A<=B<=C or C<=B<=A:
    print(B)
elif B<=A<=C or C<=A<=B:
    print(A)
elif A<=C<=B or B<=C<=A:
    print(C)
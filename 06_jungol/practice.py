# import sys; sys.stdin = open('input.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # 행 우선 순회
#     # 모든 자료의 합
#     total = 0
#     row_sum = col_sum = 0
#     for i in range(N):
#         row_sum = col_sum = 0
#         for j in range(N):
#             row_sum += arr[i][j]
#             col_sum += arr[j][i]
#         ans = min(row_sum, col_sum)
#
#     S = 0
#     for i in range(N): # 좌상단에서 우하단
#         S += arr[i][i]
#     ans = min(ans, S)
#     S = 0
#
#     for i in range(N): #우상단에서 좌하단
#         S += arr[i][N-1-i]
#
#         print(ans)
#
# import sys; sys.stdin = open('inpt.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, inpyt().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     # 모든 mxm 영역의 좌상단 좌표
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#
#             # 좌상단 i, j, 가로세로 길이 = M 사각 영역을 행우선 탐색
#             for r in range(i, i+M): # i ~ j+M-1
#                 for c in range(j, j+M): # j ~ j+M-1
#                     arr[r][c]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    row_sum = col_sum = 0
    for j in range(N):
        row_sum += arr[i][j]
        col_sum += arr[j][i]
    print(row_sum, col_sum)

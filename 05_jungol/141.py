# 1부터 100까지의 정수 중 한 개를 입력받아 100 보다 작은 배수들을 차례로 출력하다가 10 의 배수가 출력되면 프로그램을 종료하도록 프로그램을 작성하시오.

n = int(input())
result = []
for i in range(1, 11):
    if n*i % 10 != 0 and n*i < 100:
        result.append(n*i)
    elif n*i % 10 == 0 and n*i < 100:
        result.append(n*i)
        break
print(' '.join(map(str, result)))

# n = int(input())
# result = []
# result_2 = []
# for i in range(1, 11):
#     num = n * i
#     if num % 10: # 10의 배수가 아님
#         result.append(num)
#     else:
#         result.append(num)
#         break
# for i in result:
#     if i < 100 :
#         result_2.append(i)
#     else:
#         break
# print(' '.join(map(str, result_2)))

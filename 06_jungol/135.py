# 두 개의 정수를 입력받아 두 정수 사이(두 정수를 포함)에 3의 배수이거나 5의 배수인 수들의 합과 평균을 출력하는 프로그램을 작성하시오.
# (평균은 반올림하여 소수 첫째자리까지 출력한다.)

a, b = map(int, input().split())
c = []
for i in range(a, b+1):
    if i % 3 == 0 or i % 5 == 0:
        c.append(i)
print('sum: %d' % sum(c))
print('avg: {:.1f}'.format(sum(c)/len(c)))
# 10개의 정수를 입력받아 입력받은 수들 중 짝수의 개수와 홀수의 개수를 각각 구하여 출력하는 프로그램을 작성하시오.

numbers = list(map(int, input().split()))
even = []
odd = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    elif number % 2 == 1:
        odd.append(number)
print('even: %d' % len(even))
print('odd: %d' % len(odd))
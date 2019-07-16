'''
1. 두 개의 정수 n과 m이 주어질 때, 반복문을 사용하여 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 사각형을 출력하시오.
'''
n = 5
m = 9

for i in range(m):
    for j in range(n):
        print('*', end='')
    print()

'''
2. 과목명과 점수가 담긴 딕셔너리가 있을 때, 평균 점수를 출력하시오.
'''
student = {
    'python': 80, 
    'algorithm': 99, 
    'django': 89, 
    'flask': 83
}
result = 0
for score in student.values():
    result += score
print(result / len(student))

'''
3. 다음은 여러 사람의 혈액형(A, B, AB, O)에 대한 데이터이다. 반복문을 사용하여 key는 혈액형의 종류, value는 인원 수인 딕셔너리를 만들고 출력하시오.
'''
blood_types = ['A']

#1
blood_dict = {}
for blood in blood_types:
    if blood_dit.get(blood):
        blood_dict[blood] += 1
    else:
        blood_dict[blood = 1
print(blood_dict)

#2
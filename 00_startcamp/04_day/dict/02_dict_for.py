#dictionary 반복문 만들기

lunch = {
    '중국집': '02-123-1234',
    '일식집': '02-345-3456',
    '양식집': '02-234-2345'
}

# 기본 활용
for key in lunch:
    print(key)
    print(lunch[key])

# .items()
for key, value in lunch.items():
    print(key, value)

# value만 가져오기 .values()
for value in lunch.values():
    print(value)

# key만 가져오기 .keys()
for key in lunch.keys():
    print(key)
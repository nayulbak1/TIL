#dictionary 만들기 -1
lunch = {
    '중국집': '02-123-1234'
}

#만들기 -2
dinner = dict(중국집='02-123-1234', 일식집='02-345-3456')

#dictionary에 내용 추가하기
lunch['분식집'] = '02-456-4567'
print(lunch)


#dictionary 내용 가져오기
idol = {
    'bts': {
        '지민': 25, 
        'RM': 24
    }
}

# RM의 나이는?
idol['bts']['RM']
idol.get('bts').get('RM')

#dict['key']로 존재하지 않는 key를 접근할 경우 key error가 발생하지만, dict.get('key')으로 존재하지 않는 key를 접근할 경우 None 값을 넘겨줌
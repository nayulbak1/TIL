# 점심 메뉴 추천

import random

menu = ['부대찌개', '소고기', '카레']
lunch = random.choice(menu)

print(f'오늘의 점심은 {lunch}입니다.')

#로또 추천
numbers = range(1,46)
lotto = random.sample(numbers, 6)
print(f'오늘의 로또 당첨번호는 {sorted(lotto)}입니다.')

#필요 시 이렇게도 해보자
name = '박나율'
print('안녕하세요, ' + name + '입니다.')
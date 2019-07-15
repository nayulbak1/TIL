#네이버 실시간 검색어를 스크래핑 해서 txt 파일에 저장

import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com'


# 요청 보내서 html 파일 받고
html = requests.get(url).text

# BeautifulSoup으로 정제
soup = BeautifulSoup(html, 'html.parser')

# Select 메소드를 사용해서 List를 얻어낸다
names = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')

for name in names:
    print(name.text)

# 뽑은 List를 With 구문으로 잘 작성해본다. (txt)
with open('example.txt', 'w', encoding='utf-8')as f:
    for name in names:
        f.write(f'{name.text}\n')
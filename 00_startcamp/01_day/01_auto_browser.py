# import webbrowser

# 1. 리스트
# websites = ['www.google.com', 'www.naver.com']

# idols = ['bts','producex101','iu']
# url = 'https://search.naver.com/search.naver?query='

# # 2. 반복문(for) 안에서 webbrowser.open()이 실행
# # for website in websites:
#     # webbrowser.open_new(website)
# for idol in idols:
#     webbrowser.open_new(url + idol)

import requests
response = requests.get('https://www.naver.com/').status_code
print(response)
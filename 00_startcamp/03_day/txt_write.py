#변수에 만들고 싶은 파일을 open 해야 한다.
#open 할 때 r: 읽기 / w: 쓰기(+ 덮어씌워짐) / a: 추가
f = open('ssafy.txt', 'w')
for i in range(10):
    f.write(f'This is line {i+1}.\n')
f.close()

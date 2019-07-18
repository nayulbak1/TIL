# 03_homework.md

#### 1. Python에서 기본으로 사용할 수 있는 Built in function 5개를 찾아서 작성하세요. 

dir(__bilitins__)
abs()

dict()

set()

str()

sum()

![built_in](https://user-images.githubusercontent.com/18046097/61181739-2984fd80-a665-11e9-991b-f2f058397a69.png)

#### 2. 다음과 같이 함수가 정의되어 있다. 보기 중, 오류가 발생하는 코드를 고르시오. 

```python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.'')
```

```python
#1.
ssafy(location='대전', name='철수')
#2.
ssafy('길동', location='광주')
#3.
ssafy(name='허준', '구미')
```

오류가 발생하는 코드는 3번

키워드 인자 활용한 뒤에 위치 인자를 사용할 수 없다.

#### 3. 다음과 같이 코드가 작성되어 있을 때, 변수 result에 저장된 값을 작성하시오.

```python
def my_func(a,b):
    c = a + b
    print(c)
result = my_func(4,7)
```



함수에 return 값이 없어서 none
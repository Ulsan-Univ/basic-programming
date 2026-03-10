x = 5 # 정수형 5
name = "성홍제" # 문자열 "성홍제"
print(x)
print(name)

# 유효한 변수명 지정 방법
age = 21
_colour = "lilac"
total_score = 90

# [유효하지 않은 변수명 지정 방법]
# 1name = "Error" # 줄 바꿈 또는 세미콜론으로 구분해야 함a
# class = 10 # 클래스 같은 파이썬 자체에 있는 문들은 사용 X
# user-name = "Doe" #  _(언더바)를 사용해야 함

# [변수값 할당하는 방법 (변수명 = 값)]
x = 5 
y = 3.14
z = "HI"

# [동일 값 할당 방법]
a = b = c = 100
print(a, b, c)

# [서로 다른 값 할당 방법]
x, y, z = 1, 2.5, "Python"
print(x, y, z) # 교수님 추천 : 노가다처럼 하나씩 할당하기 

# [변수 형변환]
s = "10"
n = int(s) # 문자열 "10"을 정수형 10으로 변환

cnt = 5
f = float(cnt) # 정수형 5를 실수형 5.0으로 변환

age = 25
s2 = str(age) # 정수형 25를 문자열 "25"로 변환

print(n)
print(f)
print(s2)

# [변수의 유형]
n = 42 # 정수형 int
f = 3.14 # 실수형 float
s = "Hello, World!" # 문자열 string
li = [1, 2, 3] # 리스트 list
d = {'key': 'value'} # 딕셔너리 dict
b = True # 참과 거짓 bool

print(type(n))   
print(type(f)) 
print(type(s))   
print(type(li))     
print(type(d))     
print(type(b))
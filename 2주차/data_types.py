x = 50 # int 정수형
x = 60.5 # float 실수형
x = "Hello World" # str 문자형
x = ["geeks", "for", "geeks"] # list 리스트(배열)
x = ("geeks", "for", "geeks") # tuple 튜플

# 숫자형 데이터 타입
a = 5
print(type(a)) # int 정수

b = 5.0
print(type(b)) # float 실수(부동소숫점)

c = 2 + 4j 
print(type(c)) # complex 복소수

# 시퀸스 데이터 타입(연속적인 데이터의 형태)

# 문자형 데이터 타입
s = "Welcome to the Geeks World"
print(s) 

print(type(s)) # str 문자형

print(s[1]) # ["W", "e", "l", ...]을 쪼갠 것 
print(s[2]) # l
print(s[-1]) # -1은 뒤에서 부터 시작이란 뜻 그러므로 d

# 리스트 데이터 타입(배열)
a = [] # 빈 배열 생성

a = [1, 2, 3] # 배열에 정수형 값 넣기 
print(a) 

b = ["Geeks", "For", "Geeks", 4, 5] # 배열 안에는 정수, 문자를 섞어서 넣을 수 있음

a = ["Geeks", "For", "Geeks"]
print("Accessing element from the list") 
print(a[0]) # a의 0번째 요소를 출력, 즉 "Geeks" 
print(a[2]) # a의 2번째 요소를 출력, 즉 "Geeks"

print("Accessing element using negative indexing")
print(a[-1]) # 뒤에서 부터 요소를 출력, 즉 "Geeks"
print(a[-3]) # 뒤에서 부터 3번째 요소, 즉 "Geeks" 
# * 배열 안 요소를 찾을 때 배열의 크기보다 큰 숫자를 넣으면 오류가 남

# 튜플 데이터 타입
tup1 = () # 빈 튜플 생성

tup2 = ('Geeks', 'For') # 튜플 안에 요소 넣기
print("\nTuple with the use of String: ", tup2)

tup1 = (1, 2, 3, 4, 5)

print(tup1[0])
print(tup1[-1])
print(tup1[-3]) # 위 리스트와 값은 내용

# 불린 데이터 타입 
print(type(True)) 
print(type(False))
# print(type(true)) # 대소문자 구별할 것 true는 정의되지 않는다는 에러가 뜸

# Truthy / Falsy 
if 1: # 만약 1이면
  print("1 is trusthy")

if not 0: # 만약 0이 아니면
  print("0 is falsy")
# 파이썬에서는 False, 0, 0.0, None, 빈 문자열, 리스트, 튜플을 Falsy값으로 지정함. 그 외에 것들은 Truthy로 취급

# Set
s1 = set() # 빈 집합 생성

s1 = set("GeeksForGeeks") # 한 문자형이기에 G, e, e ...으로 나누어서 집합에 넣음
print("Set with the use of String: ", s1)

s2 = set(["Geeks", "For", "Geeks"]) # 배열 요소로 저장해놨기에 각 요소를 집합에 넣음 
print("Set with the use of List: ", s2) # set은 순서가 없고, 자동으로 중복된 값들은 제거함

set1 = set(["Geeks", "For", "Geeks"]) # Geeks가 겹치기에 하나 삭제
print(set1) 

for i in set1: # i에 set1의 집합 값들을 하나씩 넣기
   print(i, end=" ") # 하나씩 뒤에 공백을 주어 출력
    
print("Geeks" in set1)

# 딕셔너리 
d = {} # 빈 딕셔너리 생성

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'} # key(유일무의)와 value(변경해도 괜찮음)로 이루어짐
print(d)

d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'}) # dict 함수를 이용하여 한 줄로 딕셔너리 생성하는 방법
print(d1)

d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} # key: 1, value: Geeks ...

print(d['name']) # 'name'이라는 키 값에 대한 value를 출력

print(d.get(3)) # 3이라는 키 값에 대한 value 출력
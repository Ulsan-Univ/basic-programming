# [연산자]
a = 15
b = 4

print("더하기:", a + b) # 더하기

print("빼기:", a - b) # 빼기

print("곱하기:", a * b) # 곱하기  

print("나누기:", a / b) # 나누기 

print("나머지 없이 나누기:", a // b) # 나머지 없이 나누기  

print("나머지:", a % b) # 나머지

print("제곱:", a ** b) # 제곱

# [비교 연산자]
a = 13
b = 33

print(a > b) # a가 b보다 큼, b보다 a가 작음
print(a < b) # b가 a보다 큼, b보다 a가 작음
print(a == b) # a와 b가 같음
print(a != b) # a와 b가 다름
print(a >= b) # a가 b보다 크거나 같음, b가 a보다 작거나 같음
print(a <= b) # b가 a보다 크거나 같음, a가 b보다 작거나 같음

# [논리 연산자]
a = True
b = False
print(a and b) # a와 b 모두 True면 True, 하나라도 False면 False
print(a or b)  # a와 b 중 하나라도 True면 True, 둘 다 False면 False
print(not a)   # a가 True면 False, a가 False면 True

# [비트 연산자]
a = 10
b = 4

print(a & b) # AND
print(a | b) # OR
print(~a) # NOT
print(a ^ b) # XOR
print(a >> 2) # SHIFT >>
print(a << 2) # SHIFT <<

a = 10
b = a # b에 a를 삽입
print(b)
b += a # b = b + a
print(b) 
b -= a # b = b - a
print(b)
b *= a # b = b * a
print(b)
b <<= a # b = b << a
print(b)

# [할당 연산자]
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

# [신별 연산자] 
a = 10
b = 20
c = a

print(a is not b) # a의 값과 b의 값이 동일하지 않으면 True, 아닐 시 False
print(a is c) # a의 값과 c의 값이 동일하다면 True, 아닐 시 False

# [멤버 연산자]
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list): # x의 값이 list 안에 있지 않다면 
    print("x is NOT present in given list") # 이걸 출력
else:
    print("x is present in given list") # 아니면 이걸 출력

if (y in list): # y의 값이 list 안에 있다면
    print("y is present in given list") # 이걸 출력
else:
    print("y is NOT present in given list") # 아니면 이걸 출력
# input() 함수는 사용자 입력을 받는 데 사용

name = input("이름을 입력하세요: ")
print("Hello, ", name, "! Welcome!")

s = "Brad"
print(s)

s = "Hongjea"
age = 20
city = "ulsan"
print(s, age, city)

x, y = input("2개의 값을 입력해주세요.").split()
print("남자 수: ", x)
print("여자 수: ", y)

x, y, z = input("3개의 값을 입력하세요.").split()
print("전체 학생 수: ", x)
print("남학생 수: ", y)
print("여학생 수: ",)
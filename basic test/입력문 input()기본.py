#입력문 intput()의 기본

name = input("이름을 입력해주세요: ")
age = input("나이를 입력해주세요: ")

print("이름은", name)
print("나이는", age)

name = input("이름을 입력해주세요: ")
age = input("나이를 입력해주세요: ")

print("이름은", name)
print("나이는", age)

g_age = int(age) - 1
print("만 나이는", g_age)

#  문자 와 정수사이에 뺄셈 연산이 안되기 때문에 int 타입으로 변환 시켜서 같은 정수끼리 연산으로 변환
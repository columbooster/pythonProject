print("비만도 계산기입니다")
stature = input("키를 입력해 주세요: ")
weight = input("몸무게를 입력해 주세요: ")

stature = int(stature)
weight = int(weight)
BMI = weight/(stature*stature)*10000
#  연산순서, 더 효율적인 식 고민  힌트에는 result = a*(b+c)라고 나옴


print("신장: ", stature)
print("몸무게: ", weight )
print("BMI:" , BMI)
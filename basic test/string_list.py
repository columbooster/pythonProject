string1 = "정력 짱짱맨 남성 언더웨어"
string2 = "     25,900원     "

print(string1)
print(string2)

#  컴퓨터는 이렇게 나열된 문자 데이터의 순서에 대한 정보도 가지고 있는데 문자열의 순서 정보는 index라고 부릅니다. 여기서 주의해야할 점은 컴퓨터는 숫자를 0부터 세기 때문에 n번째 데이터의 index는 n-1이라는 것입니다.
# ex)첫번째 데이터의 index: 0

print(string1[0])
print(string1[1])
print(string1[2])

print(string1[-1])
print(string1[-2])
print(string1[-3])

# 특정위치에 있는 데이터 하나를 선택하는 것을 인덱싱(indexing)이라고 합니다. 인덱싱은 대괄호[, ]를 활용하고 변수이름[index]로 나타내며, 해당 index에 저장된 한글자를 사용할 수 있습니다.
# 음수를 활용한 마이너스(-) 인덱싱도 가능한데 index에 음수를 넣게 되면 가장 마지막 글자가 -1이 되며, 뒤에서부터 순서를 센다고 생각하면됩니다.
# 문자열의 index 범위를 넘어서는 경우에는 에러가 발생하므로 인덱싱을 할 때는 범위를 꼭 고려

print(string1[0:3])
print(string1[-2:-7])
print(string2[6:11])

print(string1[11:])
print(string1[:7])

# 슬라이싱(slicing)을 활용하면 텍스트 데이터의 일부를 잘라서 사용할 수 있습니다.
# 슬라이싱 기본형: 변수이름[index1:index2]
# 기본적으로 슬라이싱은 변수이름[index1:index2]의 모양을 가집니다. 여기서 주의해야하는 것은 첫번째 숫자는 포함하고, 두번째 숫자는 포함하지 않는 범위의 데이터가 슬라이싱되는 것입니다.

# 문자열 바꾸기: replace()
# replace()라는 함수를 사용하면 텍스트 데이터 포함된 특정 텍스트를 원하는 텍스트로 대체(replace) 할 수 있습니다.

print(string1.replace("짱짱맨","헤비"))
print(string1)

string1 = string1.replace("짱짱맨","헤비")
print(string1)

# replace()함수는 바꾸고자하는 문자열 다음에 .을 찍고 사용합니다. 파이썬에서 .은 쉽게 말하면 앞에 있는 변수와 관련된 기능을 사용하는 것이라고 생각하면 쉽습니다.

# 앞뒤공백 제거하기 : strip()

print(string2.strip())
print(string2)

string2 = string2.strip()
print(string2)

# strip()함수 같은 경우에는 별도의 명령어(입력어)가 필요없으므로 괄호 안을 비워놓습니다

# strip()한 결과 25,990원은 컴퓨터가 이해할 수 있는 데이터가 아닙니다. 유의미한 숫자데이터로 만들기 위해서는 25990의 형태로 만들어 줘야합니다. 가격데이터를 컴퓨터가 이해할 수 있는 숫자 데이터로 만들기 위해서 아래와 같이 코드를 작성
string2 = string2.replace(",","")
string2 = string2[:-1]
print(string2)

#  체이닝(Chaining)
string2 = string2.replace(",","")[:-1]
print(string2)
# 슬라이싱의 결과는 모두 문자열이기 때문에 아래와 같이 모든 기능을 한번에 이어서 쓸 수 있습니다.
#  파이썬에서 함수를 연속해서 뒤에 쓰는 것을 체이닝(Chaining)이라고 합니다. 체이닝 방식으로 코드를 구현하는 경우 코드의 길이가 짧아지지만, 아직 초보자의 레벨에서는 프로세스를 확인하기 어려우므로 파이썬 코딩에 익숙해진 후에 사용하시는 것을 권장합니다. *코드 수행속도는 크게 차이나지 않습니다



# list in python

players = ["황의조", "황희찬", "구자철", "이재성", "기성용"]

print(players)
print(players[0])
print(players[3])

print(players[-1])
print(players[-5])

# 리스트를 이용하면 위와 같이 하나의 변수에 여러가지 데이터를 저장하 사용할 수 있으며, 대괄호 [, ] 안에 데이터들을 ,로 구분하여 저장
# 저장된 데이터는 문자열 인덱싱과 같은 방법으로 데이터를 하나씩 가져올 수 있습니다. 문자열과 마찬가지로 대괄호 안에 index를 넣는 방법으로 사용할 수 있습니다.
# *문자열과 리스트는 거의 비슷한 특징을 가지고 있습니다.
# **일부 프로그래밍 언어에서 문자열은 문자(character)의 리스트로 구현되어 있습니다.

small_player = players[1:3]
print(small_player)

small_player = players[-4:-1]
print(small_player)

small_player = players[3:]
print(players)

small_player = players[:4]
print(small_player)

print(players)

players.append("이승우")
print(players)
players.append("김민재")
print(players)

del players[1]
del players[1]

print(players)

# append()함수를 사용하면 리스트에 괄호 안의 데이터를 추가할 수 있습니다. 문자열 함수와 마찬가지로 .뒤에 함수를 적어줍니다. append()함수의 특징은 데이터가 계속해서 리스트의 끝에 추가되는 것입니다.
# 데이터 삭제는 del 명령어를 통해서 할 수 있습니다. del 명령어는 다른 함수들과 다르게 괄호 안에 데이터를 삭제하는 것이 아니라 공백(space) 이후의 데이터를 삭제합니다.

# 문자열과 리스트의 길이(Length)

print(players)
print(len(players))

print(players[1])
print(len(players[1]))

# 리스트가 가지고있는 데이터의 크기는 길이(Length)라고 표현합니다. len()함수를 통해서 데이터의 길이를 알아낼 수 있습니다. 마찬가지로 문자열의 길이도 len()함수를 통해 알아낼 수 있는데, 이때는 텍스트 데이터의 길이가 출력
# 리스트/문자열의 길이를 반환합니다.
# 리스트: 포함하고있는 데이터의 수
# 문자열: 텍스트 데이터의 글자

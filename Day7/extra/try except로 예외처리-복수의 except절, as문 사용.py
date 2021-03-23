"""
try except로 예외처리하기2 (복수의 except절)

try: #예외가 발생 할 수 있는 코드
except: #문제가 생겼을 때 실행할 코드

참고: 여기서 except절 하나만 실행됨
"""

myList = [1, 2, 3]

try:
    index = int(input('index를 입력하세요: '))
    print(myList[index]/0)
except ZeroDivisionError as err: #as문 사용(예외사항에 대한 세부정보 얻고싶을때)
    print('0으로 나눌 수 없습니다.({0})'.format(err))

except IndexError as err:
    print('잘못된 index입니다.({0})'.format(err))

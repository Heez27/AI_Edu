"""
try except로 예외처리하기 (복수의 except절)
"""

myList = [1, 2, 3]

try:
    index = int(input('index를 입력하세요: '))
    print(myList[index]/0)
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

except IndexError:
    print('잘못된 index입니다. ')

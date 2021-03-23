"""
try except else로 예외처리

try: #실행할 코드 블록
except: #예외처리 코드블록
else: except절을 만나지 않았을 경우 실행됨

"""

myList = [1, 2, 3]

try:
    index = int(input('index를 입력하세요: '))
    print(myList[index])
except Exception as err:
    print('예외가 발생했습니다. ({0})'.format(err))
else:
    print('리스트 요소 출력에 성공했습니다. ')


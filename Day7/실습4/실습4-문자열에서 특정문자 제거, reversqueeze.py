"""
문자열에서 특정문자 제거한 후, reverse하는 프로그램을 작성하시오. reversqueeze 함수
-예외처리: 문자열에 제거할 문자가 없을 경우
"""

class noTarget(Exception): #제거할 문자열(target)이 없는 경우, Exception 상속
    def __init__(self, arg):
        super().__init__('제거할 문자열 {0}이/가 없습니다.'.format(arg))

def reversqueeze(text, target):#text에서 target 제거후 reverse
    if target in text:
        return text.replace(target,'')[::-1]
    else:
        raise noTarget(target)

if __name__ == '__main__':
    text = input('문자열 입력: ')
    target = input('제거할 문자열 입력: ')

    try:
        reversqueeze(text, target)
    except noTarget as err:
        print('예외 발생: {0}'.format(err))
    else:
        print('{0}에서 {1}을 제거한 결과: {2}'.format(text,target,reversqueeze(text,target)))

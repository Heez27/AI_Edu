class invalidA(Exception): #잘못된 시작지점(a)
    def __init__(self, arg):
        super().__init__('잘못된 시작지점입니다: {0}'.format(arg))
        
class invalidB(Exception): #잘못된 취할 갯수(b)
    def __init__(self, arg): 
        super().__init__('잘못된 취할갯수입니다: {0}'.format(arg))

def midstr(text, a, b): #문자열에서 a번째부터 b개를 취함
    start = int(a)
    end = int(b)
    k = start + end
    if start>= 1 and k-1 <= len(text): 
        return text[start-1:k-1]
    elif start<1 or start>len(text):
        raise invalidA(a)
    elif end<=0 or k-1 >len(text):
        raise invalidB(b)


if __name__ == '__main__':
    try:
        text = input('대상 문자열 입력: ')
        a = int(input('시작 지점 입력: '))
        b = int(input('취할 갯수 입력: '))
        midstr(text,a,b)
    except invalidA as err:
        print('예외가 발생했습니다. ({0})'.format(err))
    except invalidB as err:
        print('예외가 발생했습니다. ({0})'.format(err))
    else:
        print('결과 문자열은 {0}입니다. '.format(midstr(text,a,b)))

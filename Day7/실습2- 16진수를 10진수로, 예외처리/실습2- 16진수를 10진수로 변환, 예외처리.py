"""
16진수를 10진수로 변환, 예외처리
"""

class notHexa(Exception): #16진수 아닐때 예외처리
    def __init__(self, arg):
        super().__init__('16진수가 아닙니다. : {0}'.format(arg))

def convertToDecimal(text): #16진수를 10진수로 변환
    value = 0  #계산 결과 저장
    v = 0      #변환된 숫자 저장
    text = text.upper() #대문자로 바꿈
    for c in text:
        if (c>='0' and c<='9'):#0~9사이일 때
            v = ord(c) - ord('0') #파이썬의 입력값이 문자라서 숫자로 바꿔줌
        elif(c>='A' and c<='F'): #A~F 사이일 때(소문자는 취급 안함)
            v = ord(c) - ord('A')+10 #A~F를 10~15로 바꿔줌
        else:
            raise notHexa(text)
        value = value *16 + v
    return value
    

if __name__ == '__main__':
    try:
        text = input("16진수를 입력하시오: ")
        convertToDecimal(text)
    except notHexa as err:
        print('예외가 발생했습니다. ({0})'.format(err))
    else:
        print("16진수 {0}는 10진수 {1}입니다.".format(text,convertToDecimal(text)))

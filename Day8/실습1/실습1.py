#실습1: 텍스트 파일을 1. 암호화, 2. 복호화, 3. 파일 읽기가
#가능한 프로그램을 만드시오. 
import os
import sys

class noFile(Exception): #읽어올 파일이 없을 경우
    def __init__(self,arg):
        super().__init__('No file called, ({0}) '.format(arg))

def encode(message = ''): #암호화
    result = '' 
    for c in message:
        num = ord(c)
        result += chr(num+100)
    return result 


def decode(cipher = ''): #복호화
    result = '' 
    for c in cipher:
        num = ord(c)
        result += chr(num-100)
    return result


if __name__ == '__main__':
    menu = int(input('1. 암호화  2. 복호화  3. 파일 읽기 중 선택: '))

    if menu==1 or menu==2: #암호화 or 복호화일 경우, 입력&출력 파일 이름받음
        infname = input('입력 파일명을 입력하세요: ')
        outfname = input('출력 파일명을 입력하세요: ')
    elif menu==3: #파일 읽기, 입력파일 이름만 받음
        infname = input('파일명을 입력하세요: ')

    try:
        if not os.path.exists(infname): #파일이 없을 경우
            raise noFile(infname)

        if menu==1:#암호화
            with open(infname, 'r', encoding='utf8') as file:
                str = file.read()

            with open(outfname, 'w', encoding='utf8') as file:
                file.write(encode(str))

            print('{0} --> {1} 변환 완료'.format(infname, outfname))
            
        elif menu==2: #복호화
            with open(infname, 'r', encoding='utf8') as file:
                str = file.read()

            with open(outfname, 'w', encoding='utf8') as file:
                file.write(decode(str))

            print('{0} --> {1} 변환 완료'.format(infname, outfname))

        elif menu==3: #파일 읽기
            with open(infname,'r', encoding='utf8') as file:
                str = file.read()
            print(str)
            
    except noFile as err:
        print('예외가 발생했습니다.({0})'.format(err))


"""
문제: strcmp(s,t) 함수를 꾸며주는 deco(func)함수를 만드시오. 

-역할: s와 t의 문자열의 공백제거
"""

import sys

def deco(func):
    def stricmp(*args, **kwargs):
        s = args[0]  #데코레이트 부분(공백 제거)
        t = args[1]
        s = s.replace(' ', '') #공백을 없앰
        t = t.replace(' ', '')
        return func(s,t)#바깥함수의 입력인자로 받은 데코레이트 할 함수 리턴
    return stricmp # 실제 데코레이터 함수 이름 리턴


@deco
def strcmp(s,t):  #원래 함수
    for i in range(min(len(s),len(t))):
        a,b = ord(s[i]), ord(t[i])
        if a>b:
            return 1
        elif a < b:
            return -1
        else:
            continue

    if len(s)>len(t):
        return 1
    elif len(s) < len(t):
        return -1
    else:
        return 0
    

#메인 함수
s = input('문자열1을 입력하시오:')
t = input('문자열2을 입력하시오:')
print(strcmp(s,t))

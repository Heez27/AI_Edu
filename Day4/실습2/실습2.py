import sys
s = input("대상 문자열 입력: ")
t = input("제거할 문자 입력: ")


def revsqueeze(s,t):
    result = ''
    for i in s:   # t 제거
        if (i != t[0]):
            result = result + i

    temp = ''
    for i in result:  #reverse
        temp = i + temp

    result = temp
    return result

result = revsqueeze(s,t)

print("결과 문자열은 {0}입니다.".format(result))

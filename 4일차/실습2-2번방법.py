import sys
s = input("대상 문자열 입력: ")
t = input("제거할 문자 입력: ")


def revsqueeze(*args):
    i = 0
    result = ''
    while(i < len(args[0])):   # t 제거
        if (args[0][i] != args[1]):
            result = result + args[0][i]
        i = i+1

    result = result[ : :-1] #reverse

    return result

result = revsqueeze(s,t)

print("결과 문자열은 {0}입니다.".format(result))

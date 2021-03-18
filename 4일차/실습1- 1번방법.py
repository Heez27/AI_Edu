import sys

s = list(input("대상 문자열 입력: "))   
t = list(input("제거할 문자열 입력: ")) 

i = 0
result=[]


while(i<len(s)):
    if(s[i]!=t[0]):
        result = result + [s[i]]
    i=i+1

result.reverse()

print("결과 문자열은 {}입니다.".format(result))

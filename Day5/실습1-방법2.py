import sys

def fcmp(s,t):
    def numcmp():
        a = float(s)
        b = float(t)
        if(a>b):
            return 1
        elif (a==b):
            return 0
        else:
            return -1

    def strcmp():
        i = 0

        for i in range(min(len(s),len(t))): #앞의 문자열만 비교
            a,b = ord(s[i]), ord(t[i])
            if a>b :
                return 1
            elif a<b:
                return -1
            else:
                continue

        if len(s) > len(t):  #비교할 대상이 없으면 길이로 판단
            return 1
        elif len(s) < len(t):
            return -1
        else:
            return 0
    
        
    i = 0
    num = 0
    while(i<len(s)): #s에 문자가 있는지 체크
        if (s[i]>='0' and s[i]<='9'): #s[i]가 숫자면, 다음 문자 체크
            i = i + 1
            continue
        elif(s[i]=='-'or s[i]=='.'):#s[i]가 '-'또는 '.'면, 다음 문자 체크
            i = i + 1
            continue
        else:       #s[i]가 문자임을 확인
            num = num + 1
            break

    if(num==1):
        return strcmp
    else: #num이 0일때(s가 숫자일 때)
        while(i<len(t)): #t에 문자가 있는지 체크
            if (t[i]>='0' and t[i]<='9'): #t[i]가 숫자면, 다음 문자 체크
                i = i + 1
                continue
            elif(t[i]=='-' or t[i]=='.'):#t[i]가 '-'또는 '.'면, 다음 문자 체크
                i = i + 1
                continue
            else:        #t[i]가 문자임을 확인
                num = num + 1
                break

    if(num==0): #s와 t가 모두 숫자임
        return numcmp
    else:
        return strcmp

    
#메인 루틴
s = input("S를 입력하시오: ")
t = input("T를 입력하시오: ")

p = fcmp(s,t) #함수이름을 리턴
print(p()) 

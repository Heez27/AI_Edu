import sys
s = input("16진수를 입력하시오: ")
value = 0  #계산 결과 저장
v = 0      #변환된 숫자 저장

for c in s:  #문자열에서의 for문
    if(c>='0' and c<='9'):  #0~9사이일 때
        v = ord(c) - ord('0') #파이썬의 입력값이 문자라서 숫자로 바꿔줌
    elif(c>='A' and c<='F'): #A~F 사이일 때(소문자는 취급 안함)
        v = ord(c) - ord('A')+10 #A~F를 10~15로 바꿔줌
    else:
        print("16진수가 아닙니다.")
        sys.exit(0)
    value = value * 16 + v #***

    
print("16진수 {0}는 10진수 {1}입니다.".format(s,value))

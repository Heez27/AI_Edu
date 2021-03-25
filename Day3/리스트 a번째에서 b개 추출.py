#문자열 a번째부터 b개의 문자 추출
#리스트 요소를 붙여서 출력(str함수 이용)
import sys
s = list(input('대상 문자열 입력: '))
a = int(input('시작 지점 입력: '))
result = []

if a>len(s):
    print('문자열 길이 범위에 없습니다.')
    sys.exit(0)

b = int(input('취할 갯수 입력: '))

if b>(len(s)-a+1):
    print('문자열 범위에 포함되어있지 않습니다. ')
    sys.exit(0)
else:
    result +=s[a-1:a+b-1]
    print('result: ',end='')
    for i in result:
        print(str(i), end='') #리스트 각 요소를 str으로 변환


#문제1: 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력
#실행 결과: ‘usr’, ‘local’, ‘bin’, ‘python’
#또, 디렉토리 경로명과 파일명을 분리하여 출력
#실행 결과:‘/usr/local/‘bin’, ‘python’

s = input('경로명을 넣으시오: ')

#각각의 디렉토리 경로명을 분리: s1
s1 = s.split('/')
s1.remove('')

#디렉토리 경로명과 파일명을 분리: s2
index = s.rfind('/')
s2 = [s[:index],s[index+1:]]

print(s1)
print(s2)
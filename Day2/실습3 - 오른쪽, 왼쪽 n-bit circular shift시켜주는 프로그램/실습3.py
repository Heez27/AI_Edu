"""실습3
주어진 정수형 데이터를 왼쪽으로
n-bit circular shift 시켜주는 프로그램"""

num = int(input("number 입력: "))
n = int(input("n : "))

check = 0x8000000000000000 #2진수가 길어서 16진수로 표현
num1 = num
i = 0


while (i<64):  #num을 2진수로 표현, 실습문제2와 같음
    if((num1 & check) == 0): #num1의 맨 앞 비트가 0일 때
        print("0", end = "")
    else:                    #num1의 맨 앞 비트가 1일 때
        print("1", end = "")
                
    num1 = num1 << 1
    i = i + 1

print("\n")



i = 0
while (i < n):
    if((num & check) == 0):  #num의 맨 앞 비트가 0일 때
        num = num << 1       #그냥 시프트(산술shift는 어차피 뒤에 0붙으므로)
    else:                   #num의 맨 앞 비트가 1일 때
        num = num << 1      #왼쪽으로 shift연산 후
        num = num | 1        #num의 마지막 비트에 1추가 시킴 (1 = 0000....001)
    i = i + 1

num1 = num



i = 0

while(i<64):
    if((num1 & check) == 0):
        print("0", end = "")
    else:
        print("1", end = "")
    num1 = num1 << 1
    i = i + 1

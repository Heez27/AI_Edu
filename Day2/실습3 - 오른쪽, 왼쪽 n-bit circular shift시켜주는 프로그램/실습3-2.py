"""실습3-2
주어진 정수형 데이터를 오른쪽으로
n-bit circular shift 시켜주는 프로그램"""

num = int(input("number 입력: "))
n = int(input("n : "))

check = 0x8000000000000000
num1 = num
i = 0


while (i<64): #2진수 출력
    if((num1 & check) == 0):
        print("0", end = "")
    else:
        print("1", end = "")
                
    num1 = num1 << 1
    i = i + 1

print("\n")




i = 0
while (i < n):
    if(num >= 0): #num가 양수
        if((num & 1) == 0): #마지막 비트가 0일때
            num = num >> 1
        else:               #마지막 비트가 1일때
            num = num >> 1
            num = num | check #맨 앞 비트를 1로 만듦
        i = i + 1
    else:         #num가 음수
        if((num & 1) == 1):  #마지막 비트가 1일때
            num = num >> 1
        else:               #마지막 비트가 0일때
            num = num >> 1
            num = num & ~check # 맨 앞 비트를 0으로 만듦
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

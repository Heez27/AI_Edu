#키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요
a = input('수를 입력하세요: ')
for i in a:
    if i.isdigit()==0:
        print('정수가 아닙니다. ')
        break
    else:
        if int(a)%3 == 0:
            print('3의 배수입니다.')
            break
        else:
            print('3의 배수가 아닙니다. ')
            break
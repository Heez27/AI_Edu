#정수로 이루어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.
list = input('정수로 이루어진 리스트를 만드시오: ').split()

count = 0 #3의 배수의 개수
sum = 0 #3의 배수의 합

for i in list:
    if int(i)%3 == 0:
        count += 1
        sum += int(i)

print('주어진 리스트에서 3의 배수의 개수-> %d'%(count))
print('주어진 리스트에서 3의 배수의 합-> %d'%(sum),end='')


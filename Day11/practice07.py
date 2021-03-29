# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오
nums = list(map(int, input('5개의 정수를 입력하시오: ').split()))

#평균구하기
sum = 0
for i in nums:
    sum += i
print(sum/len(nums))
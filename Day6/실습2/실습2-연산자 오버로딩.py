"""
문제: Time 인스턴스를 생성하여 산술연산 및 비교연산 결과를
출력하는 프로그램을 만드시오.

"""

import sys
import math
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hour = hours
        self.minute = minutes
        self.second = seconds

    def getTotalSeconds(self): #초로 변환
        return self.hour*60*60 + self.minute*60 + self.second

    def fromTotalSeconds(totalSeconds = 0): #초를 시/분/초로 변환, 변수값 없으면 0
        hours = (totalSeconds // 60) //60  #self.이 안붙었으니, 지역변수(메소드안에서만 사용)
        minutes = (totalSeconds // 60) % 60
        seconds = totalSeconds % 60
        return Time(hours, minutes, seconds)
        
    def __repr__(self): # 몇시 몇분 몇초로 print
        return str(self.hour)+ '시 '+ str(self.minute)+ '분 '+ str(self.second)+ '초'

    def __add__(self, other): #객체 사이의 + 연산자 재정의
        totalSeconds = abs(self.getTotalSeconds() + other.getTotalSeconds())
        return Time.fromTotalSeconds(totalSeconds)

    def __sub__(self, other): #객체 사이의 - 연산자 재정의
        totalSeconds = abs(self.getTotalSeconds() - other.getTotalSeconds())
        return Time.fromTotalSeconds(totalSeconds)

    def __lt__(self, other):  #객체 사이의 < 연산자 재정의
        return self.getTotalSeconds() < other.getTotalSeconds()
    def __gt__(self, other):  #객체 사이의 > 연산자 재정의
        return self.getTotalSeconds() > other.getTotalSeconds()
    def __eq__(self, other):  #객체 사이의 == 연산자 재정의
        return self.getTotalSeconds() == other.getTotalSeconds()


#메인 함수
t1h, t1m, t1s = input('t1 입력 [시 분 초]: ').split()
t2h, t2m, t2s = input('t2 입력 [시 분 초]: ').split()
t1 = Time(int(t1h), int(t1m), int(t1s))
t2 = Time(int(t2h), int(t2m), int(t2s))

print('t1: ', t1)
print('t2: ', t2)
print('t1 + t2: ', t1+t2)
print('t1 - t2: ', t1-t2)
print('t1 > t2: ', t1>t2)
print('t1 < t2: ', t1<t2)
print('t1 == t2: ', t1==t2)

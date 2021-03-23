"""
Strcmp(문자열 비교 함수)와 Numcmp(숫자 비교 함수)를
추상기반클래스 (Compare함수)를 이용해 만드시오.
"""

from abc import ABCMeta  #추상기반 클래스 위해 무조건 써줌
from abc import abstractmethod

class Compare(metaclass = ABCMeta): #metaclass = ABCMeta: 추상기반 클래스 명시
    def __init__(self, s, t):
         self.s = s
         self.t = t
    @abstractmethod #추상메소드, 자식클래스에서 재정의 필요 
    def cmp(self):#비교하는 함수
        pass


class Strcmp(Compare): #문자열 비교. Compare함수 상속
    def cmp(self):
        i = 0
        while i < len(self.s) and i < len(self.t): #s와 t중 짧은 index까지
            if ord(self.s[i]) < ord(self.t[i]): 
                return -1
            elif ord(self.s[i]) > ord(self.t[i]):
                return 1
            i += 1


        if len(self.s) < len(self.t): # 문자열 t가 더 길때
            return -1
        elif len(self.s) > len(self.t):# 문자열 s가 더 길때
            return 1
        else:
            return 0


class Numcmp(Compare): #숫자 비교, Compare함수 상속
    def cmp(self): 
        s_temp = float(self.s)
        t_temp = float(self.t)

        if s_temp > t_temp: 
            return 1
        elif s_temp < t_temp:
            return -1


if __name__ == '__main__':
    A = Strcmp('abc','abd')
    print('Strcmp abc & abd: {0}'.format(A.cmp()))
    B = Numcmp(23, 57)
    print('Numcmp 23 & 57: {0}'.format(B.cmp()))

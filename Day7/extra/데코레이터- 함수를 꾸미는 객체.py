"""
데코레이터: 함수를 꾸미는 객체 pg.28
"""

class MyDecorator:
    def __init__(self,f):
        print('initializing My Decorator..')
        self.func = f

    def __call__(self):
        print('Begin: {}'.format(self.func.__name__))
        self.func() #호출 반드시 있어야돼
        print('End:{}'.format(self.func.__name__))


@MyDecorator
def print_hello():
    print('Hello.')


print_hello() #MyDecorator(print_hello)()
              # __call__메서드가 함수형 데코레이터 역할

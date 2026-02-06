'''
원의 반지름을 입력받아 원의 넓이와 둘레를 계산하는 프로그램을 작성하세요. (π = 3.14159 사용)
출력결과:
원의 반지름을 입력하세요: 5
반지름이 5인 원의 넓이: 78.54
반지름이 5인 원의 둘레: 31.42
'''
#import numpy as np
#pi = round(np.pi,6)
pi = 3.14159

def sol(num):
    print(f'반지름이 {num}인 원의 넓이: {round(num*num*pi,2)}')
    print(f'반지름이 {num}인 원의 둘레: {round(2*num*pi,2)}')

number = input("원의 반지름을 입력하세요: ")
number = float(number)
sol(number)
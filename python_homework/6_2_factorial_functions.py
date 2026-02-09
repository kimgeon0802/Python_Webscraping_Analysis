'''
팩토리얼을 계산하는 재귀함수와 반복문을 사용한 함수를 각각 작성하세요.
출력결과:
5! (재귀) = 120
5! (반복) = 120
7! (재귀) = 5040
7! (반복) = 5040
'''

def rec_(n):
    if n > 1:
        return n * rec_(n-1)
    else:
        return 1

def for_(n):
    re = 1
    for i in range(1,n+1):
        re *= i

    return re

print(f'{5}! (재귀) = {rec_(5)}')
print(f'{5}! (반복) = {for_(5)}')
print(f'{7}! (재귀) = {rec_(7)}')
print(f'{7}! (반복) = {for_(7)}')
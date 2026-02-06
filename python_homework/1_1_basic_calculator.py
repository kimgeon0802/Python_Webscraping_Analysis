'''
사용자로부터 두 개의 정수를 입력받아 사칙연산(+, -, *, /)의 결과를 출력하는 프로그램을 작성하세요.
출력결과:
첫 번째 숫자를 입력하세요: 10
두 번째 숫자를 입력하세요: 3
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.33
'''
def sol(num1, num2):
    a = num1+num2
    b = num1-num2
    c = num1*num2
    d = num1/num2
    print(f'{num1} + {num2} = {a}')
    print(f'{num1} - {num2} = {b}')
    print(f'{num1} * {num2} = {c}')
    print(f'{num1} / {num2} = {round(d,2)}')

number1 = input("첫 번째 숫자를 입력하세요: ")
number2 = input("두 번째 숫자를 입력하세요: ")
number1 = int(number1)
number2 = int(number2)
sol(number1, number2)
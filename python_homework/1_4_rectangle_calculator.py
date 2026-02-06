'''
직사각형의 가로와 세로 길이를 입력받아 넓이와 둘레를 계산하는 프로그램을 작성하세요.
출력결과:
가로 길이를 입력하세요: 8
세로 길이를 입력하세요: 5
직사각형의 넓이: 40
직사각형의 둘레: 26
'''
def sol(num1, num2):
    a = num1*num2
    b = (2*num1)+(2*num2)
    print(f'직사각형의 넓이: {a}')
    print(f'직사각형의 둘레: {b}')

number1 = input("가로 길이를 입력하세요: ")
number2 = input("세로 길이를 입력하세요: ")
number1 = int(number1)
number2 = int(number2)
sol(number1, number2)

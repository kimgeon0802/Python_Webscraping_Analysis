'''
상품의 가격과 할인율을 입력받아 할인된 가격을 계산하는 프로그램을 작성하세요.
출력결과:
상품 가격을 입력하세요: 50000
할인율을 입력하세요(%): 20
원래 가격: 50000원
할인율: 20%
할인 금액: 10000원
최종 가격: 40000원
'''
def sol(num1, num2):
    a = (num1/100)*num2
    b = num1 - a

    print(f'원래 가격: {num1}')
    print(f'할인율: {num2}')
    print(f'할인 금액: {int(a)}')
    print(f'최종 가격: {int(b)}')

number1 = input("상품 가격을 입력하세요: ")
number2 = input("할인율을 입력하세요(%): ")
number1 = int(number1)
number2 = int(number2)
sol(number1, number2)
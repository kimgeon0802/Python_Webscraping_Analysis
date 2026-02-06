'''
섭씨 온도를 입력받아 화씨 온도로 변환하는 프로그램을 작성하세요. (화씨 = 섭씨 * 9/5 + 32)
출력결과:
섭씨 온도를 입력하세요: 25
섭씨 25도는 화씨 77.0도입니다.
'''
def sol(num):
    a = num*9/5+32
    print(f'섭씨 {num}도는 화씨 {round(a,1)}도입니다.')

number = input("섭씨 온도를 입력하세요: ")
number = int(number)
sol(number)
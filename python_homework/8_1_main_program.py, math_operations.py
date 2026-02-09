'''
수학 연산을 위한 모듈을 만들고 이를 사용하는 메인 프로그램을 작성하세요.
출력결과:
원의 넓이: 78.54
직사각형 넓이: 50
팩토리얼 5! = 120
최대공약수(48, 18) = 6
'''
import testmodule

cir_ = 5
rect_w, rect_h = 10, 5
fac_ = 5
num1, num2 = 48, 18

print(f"원의 넓이: {testmodule.cir(cir_):.2f}")
print(f"직사각형 넓이: {testmodule.rec(rect_w, rect_h)}")
print(f"팩토리얼 {fac_}! = {testmodule.fac(fac_)}")
print(f"최대공약수({num1}, {num2}) = {testmodule.gcd(num1, num2)}")
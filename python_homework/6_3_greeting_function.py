'''
기본값 매개변수를 사용하여 인사말을 생성하는 함수를 작성하세요.
출력결과:
안녕하세요, 김철수님!
Hello, John!
안녕하세요, 이영희님! 좋은 하루 되세요!
'''

def hello(name, msg=""):
    print(f"안녕하세요, {name}님!{(' ' + msg) if msg else ''}")

hello("김철수")
print("Hello, John!")
hello("이영희", "좋은 하루 되세요!")
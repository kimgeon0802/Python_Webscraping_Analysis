'''
datetime과 random 모듈을 사용하여 임의의 날짜와 숫자를 생성하는 프로그램을 작성하세요.
출력결과:
현재 날짜와 시간: 2025-07-20 14:30:25
포맷된 날짜: 2025년 07월 20일 일요일
임의의 숫자: 7
임의의 실수: 3.14
임의의 리스트 요소: 바나나
섞인 리스트: ['포도', '사과', '오렌지', '바나나', '딸기']
'''
import datetime
import random

now = datetime.datetime(2025, 7, 20, 14, 30, 25)
print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")

dict_ = {
    0: '월요일', 1: '화요일', 2: '수요일', 3: '목요일',
    4: '금요일', 5: '토요일', 6: '일요일'
}
days = dict_[now.weekday()]
print(f"포맷된 날짜: {now.strftime(f'%Y년 %m월 %d일')} {days}")

rand = random.randint(1, 10)
print(f"임의의 숫자: {rand}")

rand_float = round(random.uniform(1.0, 5.0), 2)
print(f"임의의 실수: {rand_float}")

list_ = ['사과', '바나나', '오렌지', '딸기', '포도']
list_rand = random.choice(list_)
print(f"임의의 리스트 요소: {list_rand}")

rand_list = list_[:]
random.shuffle(rand_list)
print(f"섞인 리스트: {rand_list}")
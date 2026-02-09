'''
f-string을 사용한 문자열 포매팅 예제를 작성하세요.
출력결과:
이름: 김철수, 나이: 25
원주율: 3.14
가격: 1,234원
퍼센트: 85.50%
날짜: 2025년 07월 20일
'''

name = "김철수"
age = 25
pi = 3.141592
price = 1234
percent = 85.5
year = 2025
month = 7
day = 20

print(f"이름: {name}, 나이: {age}")
print(f"원주율: {pi:.2f}")
print(f"가격: {price:,}원")
print(f"퍼센트: {percent:.2f}%")
print(f"날짜: {year}년 {month:02d}월 {day:02d}일")
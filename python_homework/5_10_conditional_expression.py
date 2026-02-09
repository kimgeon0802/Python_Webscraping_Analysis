'''
삼항 연산자와 조건부 표현식을 사용하는 예제를 작성하세요.
출력결과:
점수: 85, 결과: 합격
나이: 17, 상태: 미성년자
숫자들의 최대값: 42
양수들: [5, 12, 8, 23]
'''
score = 85
result = "합격" if score >= 60 else "불합격"
print(f"점수: {score}, 결과: {result}")

age = 17
st = "성년자" if age >= 18 else "미성년자"
print(f"나이: {age}, 상태: {st}")

numbers = [12, 7, 42, 3]
max_ = max(numbers) if numbers else None
print(f"숫자들의 최대값: {max_}")

rand_= [5, -3, 12, 0, 8, -1, 23]
po = [num for num in mix_ if num > 0]
print(f"양수들: {po}")
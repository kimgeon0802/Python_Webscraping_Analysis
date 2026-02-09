'''
리스트의 통계 정보(평균, 최댓값, 최솟값, 표준편차)를 반환하는 함수를 작성하세요.
출력결과:
숫자들: [10, 20, 30, 40, 50]
평균: 30.0
최댓값: 50
최솟값: 10
표준편차: 15.81
'''

def sol(numbers):
    avg_ = sum(numbers) / len(numbers)
    max_ = max(numbers)
    min_ = min(numbers)
    var_ = sum((x - avg_) ** 2 for x in numbers) / (len(numbers) - 1)
    std_ = var_ ** 0.5
    
    print(f"숫자들: {numbers}")
    print(f"평균: {avg_:.1f}")
    print(f"최댓값: {max_}")
    print(f"최솟값: {min_}")
    print(f"표준편차: {std_:.2f}")

nums = [10, 20, 30, 40, 50]
sol(nums)
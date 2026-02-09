'''
5개의 숫자를 리스트에 저장하고 합계와 평균을 구하는 프로그램을 작성하세요.
출력결과:
숫자들: [10, 20, 30, 40, 50]
합계: 150
평균: 30.0
'''
n_list = [10, 20, 30, 40, 50]
print(f'숫자들: {n_list}')

sum_ = 0
for i in range(0,len(n_list)):
    sum_ += n_list[i]

print(f'합계: {sum_}')

aver_ = sum_ / len(n_list)
print(f'합계: {aver_}')
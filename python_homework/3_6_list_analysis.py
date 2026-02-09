'''
리스트에서 최댓값, 최솟값, 두 번째로 큰 값을 찾는 프로그램을 작성하세요.
출력결과:
숫자 목록: [15, 3, 27, 8, 19, 12, 31]
최댓값: 31
최솟값: 3
두 번째로 큰 값: 27
'''

num_list = [15, 3, 27, 8, 19, 12, 31]
max_ = max(num_list)
min_ = min(num_list)
for i in range(0,len(num_list)):
    if num_list[i] == max_:
        del num_list[i]

print(f'최댓값: {max_}')
print(f'최솟값: {min_}')
print(f'두 번째로 큰 값: {max(num_list)}')
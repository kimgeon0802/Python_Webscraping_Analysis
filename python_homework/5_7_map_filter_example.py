'''
map과 filter를 사용하여 리스트를 처리하는 프로그램을 작성하세요.
출력결과:
원본 숫자: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
모든 수의 제곱: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
5보다 큰 수들: [6, 7, 8, 9, 10]
5보다 큰 수들의 제곱: [36, 49, 64, 81, 100]
'''

list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a_list = list(map(lambda x: x**2,list_))
b_list = list(filter(lambda x: x>5, list_))
c_list = list(map(lambda x: x**2, b_list))

print(f'원본 숫자: {list_}')
print(f'모든 수의 제곱: {a_list}')
print(f'5보다 큰 수들: {b_list}')
print(f'5보다 큰 수들의 제곱: {c_list}')
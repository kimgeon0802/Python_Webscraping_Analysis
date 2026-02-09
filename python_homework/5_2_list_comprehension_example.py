'''
리스트에서 짝수만 추출하여 제곱하는 코드를 리스트 컴프리헨션으로 작성하세요.
출력결과:
원본 리스트: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
짝수들: [2, 4, 6, 8, 10]
짝수의 제곱: [4, 16, 36, 64, 100]
'''

list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ev_list = []
ev_list1 = []
for i in list_:
    if i % 2 == 0:
        ev_list.append(i)
        ev_list1.append(i**2)


print(f'원본 리스트: {list_}')
print(f'짝수들: {ev_list}')
print(f'짝수의 제곱: {ev_list1}')
'''
두 개의 리스트를 병합하고 공통 요소를 찾는 프로그램을 작성하세요.
출력결과:
리스트1: [1, 2, 3, 4, 5]
리스트2: [4, 5, 6, 7, 8]
병합된 리스트: [1, 2, 3, 4, 5, 6, 7, 8]
공통 요소: [4, 5]
'''

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

list_ = []
for i in list1:
    for j in list2:
        if i == j:
            list_.append(i)

print(f'리스트1: {list1}')
print(f'리스트2: {list2}')

list1.extend(list2)

print(f'병합된 리스트: {list(set(list1))}')
print(f'공통 요소: {list_}')

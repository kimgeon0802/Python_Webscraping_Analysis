'''
any와 all 함수를 사용하여 조건을 검사하는 프로그램을 작성하세요.
출력결과:
숫자 리스트: [2, 4, 6, 8, 10]
모든 수가 짝수인가? True
하나라도 10보다 큰 수가 있는가? False

숫자 리스트2: [1, 3, 5, 7, 12]
모든 수가 짝수인가? False
하나라도 10보다 큰 수가 있는가? True
# any_all_example.py
numbers1 = [2, 4, 6, 8, 10]
numbers2 = [1, 3, 5, 7, 12]
'''

numbers1 = [2, 4, 6, 8, 10]
numbers2 = [1, 3, 5, 7, 12]

check_list1 = []
check_list2 = []
for i in numbers1:
    if i % 2 == 0:
        check_list1.append(True)
    else:
        check_list1.append(False)

    if i > 10:
        check_list2.append(True)
    else:
        check_list2.append(False)

print(f'숫자 리스트: {numbers1}')
print(f'모두가 짝수인가? {all(check_list1)}')
print(f'하나라도 10보다 큰 수가 있는가? {any(check_list2)}')

check_list1 = []
check_list2 = []
for i in numbers2:
    if i % 2 == 0:
        check_list1.append(True)
    else:
        check_list1.append(False)

    if i > 10:
        check_list2.append(True)
    else:
        check_list2.append(False)

print(f'숫자 리스트: {numbers2}')
print(f'모두가 짝수인가? {all(check_list1)}')
print(f'하나라도 10보다 큰 수가 있는가? {any(check_list2)}')
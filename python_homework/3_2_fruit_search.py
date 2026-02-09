'''
과일 이름들이 담긴 리스트에서 특정 과일을 검색하는 프로그램을 작성하세요.
출력결과:
과일 목록: ['사과', '바나나', '오렌지', '포도', '딸기']
찾을 과일을 입력하세요: 바나나
'바나나'가 목록에 있습니다!
'''

s_list = ['사과', '바나나', '오렌지', '포도', '딸기']
print(f"과일 목록: {s_list}")
s = input("찾을 과일을 입력하세요: ")

check_count = 0
for i in range(0,len(s_list)):
    if s == s_list[i]:
        check_count += 1

if check_count != 0:
    print(f"'{s}'가 목록에 있습니다!")
else:
    print(f"'{s}'가 목록에 없습니다.")
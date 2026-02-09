'''
이메일 주소를 입력받아 @ 기호를 기준으로 사용자명과 도메인을 분리하여 출력하는 프로그램을 작성하세요.
출력결과:
이메일 주소를 입력하세요: user@example.com
사용자명: user
도메인: example.com
'''

def sol(stri):
    stri_list = stri.split("@")
    print(f'사용자명: {stri_list[0]}')
    print(f'도메인: {stri_list[1]}')

stri_ = input("이메일 주소를 입력하세요: ")
sol(stri_)
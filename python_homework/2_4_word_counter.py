'''
문장을 입력받아 공백을 제거하고, 단어의 개수를 세는 프로그램을 작성하세요.
출력결과:
문장을 입력하세요:   Python is   great   
공백 제거: Python is great
단어 개수: 3개
'''

def sol(stri):
    #stri = stri.replace("  ", " ")
    stri_list = stri.split(" ")
    stri_list = [x for x in stri_list if x and x.strip()]
    print(stri_list)
    stri1 = ""
    for i in range(0,len(stri_list)):
        if i == len(stri_list):
            stri1 += stri_list[i]

        else:
            stri1 += stri_list[i]+" "

    print(f'공백 제거: {stri1}')
    print(f'단어 개수: {len(stri_list)}')


stri_ = input('문장을 입력하세요: ')
sol(stri_)
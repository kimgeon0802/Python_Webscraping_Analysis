'''
텍스트 파일의 단어 빈도를 계산하는 프로그램을 작성하세요.
출력결과:
단어 빈도 분석 결과:
파이썬: 3번
프로그래밍: 2번  
언어: 2번
배우기: 1번
쉬운: 1번
강력한: 1번
'''

from collections import Counter

ex_text = """
파이썬은 쉬운 프로그래밍 언어입니다.
파이썬은 강력한 프로그래밍 언어입니다.
파이썬 배우기는 재미있습니다.
"""

text = ex_text.replace("\n", " ").replace(".", "").split()
count = Counter(text)

print("단어 빈도 분석 결과:")
for text_, count_ in count.most_common():
    print(f"{text_}: {count_}번")
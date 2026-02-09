'''
텍스트 파일에 여러 줄의 문자열을 저장하고 읽어오는 프로그램을 작성하세요.
출력결과:
파일에 저장할 내용:
안녕하세요
파이썬 파일 처리를 연습하고 있습니다
오늘은 좋은 날씨입니다

파일에서 읽어온 내용:
안녕하세요
파이썬 파일 처리를 연습하고 있습니다
오늘은 좋은 날씨입니다
'''

texts = [
    "안녕하세요",
    "파이썬 파일 처리를 연습하고 있습니다",
    "오늘은 좋은 날씨입니다"
]

print("파일에 저장할 내용:")
for text in texts:
    print(text)

with open("data/test.txt", "w", encoding="utf-8") as f:
    for text in texts:
        f.write(text + "\n")

print("\n파일에서 읽어온 내용:")
with open("data/test.txt", "r", encoding="utf-8") as f:
    for text in f:
        print(text.strip())
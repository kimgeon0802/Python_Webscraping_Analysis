'''
JSON 형태의 데이터를 파일에 저장하고 읽어오는 프로그램을 작성하세요.
출력결과:
데이터가 data.json에 저장되었습니다.

JSON에서 읽어온 데이터:
이름: 김철수
나이: 25
직업: 개발자
취미: ['독서', '영화감상', '코딩']
주소: 서울시 강남구
'''
import pandas as pd

data = {
    "이름": ["김철수"],
    "나이": [25],
    "직업": ["개발자"],
    "취미": [["독서", "영화감상", "코딩"]],
    "주소": ["서울시 강남구"]
}
df = pd.DataFrame(data)

df.to_json("/data/test.json")

print("데이터가 test.json에 저장되었습니다.\n")

df_read = pd.read_json("/data/test.json")

print("JSON에서 읽어온 데이터:")
for col in df_read.columns:
    print(f"{col}: {df_read.iloc[0][col]}")
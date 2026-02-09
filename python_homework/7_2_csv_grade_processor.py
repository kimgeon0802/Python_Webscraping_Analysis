'''
CSV 형태의 학생 성적 데이터를 파일에 저장하고 읽어서 평균을 계산하는 프로그램을 작성하세요.
출력결과:
학생 성적이 grades.csv에 저장되었습니다.

성적 분석 결과:
김철수: 85점
이영희: 92점  
박민수: 78점
최수진: 95점
전체 평균: 87.5점
'''

import pandas as pd

data = {
    "이름": ["김철수", "이영희", "박민수", "최수진"],
    "성적": [85, 92, 78, 95]
}

df = pd.DataFrame(data)

df.to_csv("/data/grades.csv", index=False, encoding="utf-8-sig")

print("학생 성적이 grades.csv에 저장되었습니다.\n")

df_read = pd.read_csv("grades.csv", encoding="utf-8-sig")

print("성적 분석 결과:")
for idx, row in df_read.iterrows():
    print(f"{row['이름']}: {row['성적']}점")

avg = df_read["성적"].mean()
print(f"전체 평균: {average:.1f}점")
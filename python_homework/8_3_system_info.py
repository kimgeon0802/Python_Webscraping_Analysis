'''
os와 sys 모듈을 사용하여 시스템 정보를 출력하고 파일 경로를 다루는 프로그램을 작성하세요.
출력결과:
현재 작업 디렉토리: /Users/username/python_practice
Python 버전: 3.9.7 (default, Oct 13 2021, 06:44:56)
운영체제: posix
환경 변수 PATH 일부: /usr/local/bin:/usr/bin:/bin
파일 경로 정보:
- 디렉토리: /Users/username/documents
- 파일명: report.txt
- 확장자: .txt
파일 존재 여부: False
'''

import os
import sys

pwd_dir = os.getcwd()
python_ver = sys.version
os_name = os.name
path_env = os.environ["PATH"][0:50]

file_path = "testmodule.py"
dir_path, file_name = os.path.split(file_path)
file_root, file_ext = os.path.splitext(file_name)
file_exists = os.path.exists(file_path)

print(f"현재 작업 디렉토리: {pwd_dir}")
print(f"Python 버전: {python_ver}")
print(f"운영체제: {os_name}")
print(f"환경 변수 PATH 일부: {path_env}")
print("파일 경로 정보:")
print(f"- 디렉토리: {dir_path}")
print(f"- 파일명: {file_name}")
print(f"- 확장자: {file_ext}")
print(f"파일 존재 여부: {file_exists}")
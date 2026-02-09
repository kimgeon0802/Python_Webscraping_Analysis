'''
단어들이 담긴 리스트에서 가장 긴 단어와 가장 짧은 단어를 찾는 프로그램을 작성하세요.
출력결과:
단어 목록: ['cat', 'elephant', 'dog', 'butterfly', 'ant']
가장 긴 단어: butterfly (9글자)
가장 짧은 단어: cat (3글자)
'''

a = ['cat', 'elephant', 'dog', 'butterfly', 'ant']
l = max(a, key=len)
s = min(a, key=len)

print(f'단어 목록: {a}')
print(f'가장 긴 단어: {l}')
print(f'가장 짧은 단어: {s}')
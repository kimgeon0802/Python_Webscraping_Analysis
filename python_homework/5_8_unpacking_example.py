'''
언패킹과 *args, **kwargs를 사용하는 예제를 작성하세요.
출력결과:
좌표: x=10, y=20
리스트 언패킹: a=1, b=2, c=3
가변 인수의 합: 60
키워드 인수들: name=김철수, age=25, city=서울
'''

def tuple_unpacking(x, y):
    print(f"좌표: x={x}, y={y}")

coords = (10, 20)
tuple_unpacking(*coords)

def list_unpacking(a, b, c):
    print(f"리스트 언패킹: a={a}, b={b}, c={c}")

lst = [1, 2, 3]
list_unpacking(*lst)

def ex_args(*args):
    print(f"가변 인수의 합: {sum(args)}")

ex_args(10, 20, 30)

def ex_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"키워드 인수들: {key}={value}", end=', ')
    
ex_kwargs(name="김철수", age=25, city="서울")

'''
def all_together(x, y, *args, **kwargs):
    print(f"좌표: x={x}, y={y}")
    print(f"리스트 언패킹: a={args[0]}, b={args[1]}, c={args[2]}")
    print(f"가변 인수의 합: {sum(args)}")
    kw_str = ', '.join([f"{k}={v}" for k, v in kwargs.items()])
    print(f"키워드 인수들: {kw_str}")

tup = (10, 20)
lst = [1, 2, 3]

all_together(*tup, *lst, name="김철수", age=25, city="서울")
'''
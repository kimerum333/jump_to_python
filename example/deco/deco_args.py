import time

def elapsed(original_func):
    # 전달받은 인자를 래퍼에도 전달해야한다.
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print(f"지나간 시간 : {float(end-start)}")
        return result
    return wrapper

# 인자를 전달한다.
@elapsed
def myfunc(msg: str):
    print(f"{msg} 를 출력합니다.")

# closure = elapsed(myfunc)
# closure()

myfunc("이것이 데코레이션")
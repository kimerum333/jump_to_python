import time

def myfunc():
    start = time.time()
    print("함수가 실행됩니다.")
    end = time.time()
    print(f"수행 시간 : {float(end-start)}초")

myfunc()
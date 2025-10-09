# 문자열 관련 함수인 upper() 를 사용하여 프로그램 실행 시 전달된 인수를 모두 대문자로 바꾸어 주는 간
# 단한 프로그램이다. 명령 프롬프트 창에서 다음과 같이 실행해 보자.
# sys2.py 파일이 C:\doit 디렉터리 안에 있어야만 한다.
# C:\doit>python sys2.py life is too short, you need python
import sys
def to_upper():
    args = sys.argv[1:]
    bargs = " ".join(args).upper()
    print(bargs)

def dbug():
    f1 = open("test.txt", 'w')
    f1.write("Life is too short")
    f1.close()
    f2 = open("test.txt", 'r')
    print(f2.read())

def save_input():
    user_input = input("여기에 저장할 내용을 입력하세요 : ")
    f = open("test2.txt","a")
    f.write(user_input)
    f.write("\n")
    f.close

def change_file():
    f1 = open("test3.txt","w",encoding="utf-8")
    f1.write("Life is too short\n")
    f1.write("you need java")
    f1.close()

    f2 = open("test3.txt",'r')
    body = f2.read().replace("java","python")
    f2.close()
    f3 = open("test3.txt",'w')
    f3.write(body)
    f3.close

def myargv():
    args = sys.argv[1:]
    total = 0
    for arg in args:
        total += int(arg)
    print(total)
    
if __name__ == "__main__":
    myargv()
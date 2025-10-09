# 1
# 홍길동 씨의 평균 점수 구하기
def mean():
    korean = 80
    english = 75
    math = 55
    return (korean + english + math) / 3
# 2
## 짝홀판별
def is_odd(number: int):
    if(number % 2==1):
        return "odd"
    else:
        return "even"
# Q3 주민등록번호 나누기
# 홍길동 씨의 주민등록번호는 881120‑1068234 이다. 홍길동 씨의 주민등록번호를 연월일 (YYYYMMDD)
# 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
# pin = "881120-1068234"
# yyyymmdd = <이 곳 을 완 성 하 세 요 >
# num = <이 곳 을 완 성 하 세 요 >
# print(<이 곳 을 완 성 하 세 요 >) # 연 월 일 부 분 출 력
# print(<이 곳 을 완 성 하 세 요 >) # 숫 자 부 분 출 력
# 문자열 슬라이싱 기법을 사용해 보자

def slice_pin():
    pin = "881120-1068234"
    yyyymmdd = pin[0:6]
    num = pin[7:]
    print(yyyymmdd) # 연 월 일 부 분 출 력
    print(num) # 숫 자 부 분 출 력

# Q4 주민등록번호 인덱싱
# 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를
# 출력해 보자.
# pin = "881120-1068234"
# print(<이 곳 을 완 성 하 세 요 >)
# 문자열 인덱싱을 사용해 보자.
def index_pin():
    pin = "881120-1068234"
    print(pin[7])

# Q5 문자열 바꾸기
# 다음과 같은 문자열 a:b:c:d 가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d 로 바꿔 출력해 보자.
# a = "a:b:c:d"
# b = <이 곳 을 완 성 하 세 요 >
# print(b) # 문 자 열 "a#b#c#d" 출 력

def swap_str():
    a = "a:b:c:d"
    b = a.replace(":","#")
    print(b) # 문 자 열 "a#b#c#d" 출 력

# Q6 리스트 역순 정렬하기
# [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1] 로 만들어 보자.
# a = [1, 3, 5, 4, 2]
# a.<이 곳 을 완 성 하 세 요 > # [1, 2, 3, 4, 5]로 변 경
# a.<이 곳 을 완 성 하 세 요 > # [5, 4, 3, 2, 1]로 변 경
# print(<이 곳 을 완 성 하 세 요 >)
# 리스트의 내장 함수를 사용해 보자.

def reverser():
    a = [1, 3, 5, 4, 2]
    a.sort() # [1, 2, 3, 4, 5]로 변 경
    a.reverse() # [5, 4, 3, 2, 1]로 변 경
    print(a)

# Q7 리스트를 문자열로 만들기
# [‘Life’, ‘is’, ‘too’, ‘short’] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
# a = [ ‘ Life ’ , ‘ is ’ , ‘ too ’ , ‘ short ’ ]
# result = <이 곳 을 완 성 하 세 요 >
# print(result) # "Life is too short" 출 력
# 문자열의 join 함수를 사용하면 리스트를 문자열로 쉽게 만들 수 있다.

def joiner():
    a = ["Life", "is", "too", "short"]
    result = " ".join(a)
    print(result) # "Life is too short" 출 력


#     Q8 튜플 더하기
# (1, 2, 3) 튜플에 값 4 를 추가하여 (1, 2, 3, 4) 를 만든 후 출력해 보자.
# a = (1, 2, 3)
# a = <이 곳 을 완 성 하 세 요 >
# print(a) # (1, 2, 3, 4) 출 력
# 더하기 (+) 연산을 사용해 보자.

def tuple_adder():
    a = (1, 2, 3)
    a = a + tuple([4])
    print(a) # (1, 2, 3, 4) 출 력

# Q9 딕셔너리의 키
# 다음과 같은 딕셔너리 a 가 있다.
# >>> a = dict()
# >>> a
# {}
# 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.
# a['name'] = 'python'
# a[('a',)] = 'python'
# a[[1]] = 'python'
# a[250] = 'python'

# Q10 딕셔너리 값 추출하기
# 딕셔너리 a 에서’B’ 에 해당하는 값을 추출해 보자.
# a = {'A':90, 'B':80, 'C':70}
# result = <이 곳 을 완 성 하 세 요 >
# print(a) # {'A':90, 'C':70} 출 력
# print(result) # 80 출 력
# 딕셔너리의 pop 함수를 사용해 보자.
def extractor():
    a = {'A':90, 'B':80, 'C':70}
    result = a.pop('B')
    print(a) # {'A':90, 'C':70} 출 력
    print(result) # 80 출 력

# Q11 리스트에서 중복 제거하기
# a 리스트에서 중복 숫자를 제거해 보자.
# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# aSet = <이 곳 을 완 성 하 세 요 > # a 리 스 트 를 집 합 자 료 형 으 로 변 환
# b = <이 곳 을 완 성 하 세 요 > # 집 합 자 료 형 을 리 스 트 자 료 형 으 로 다 시 변 환
# print(b) # [1, 2, 3, 4, 5] 출 력
# 집합 자료형의 요솟값이 중복될 수 없다는 특징을 사용해 보자.

def duplicate_breaker():
    a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
    aSet = set(a) # a 리 스 트 를 집 합 자 료 형 으 로 변 환
    b = list(aSet) # 집 합 자 료 형 을 리 스 트 자 료 형 으 로 다 시 변 환
    print(b) # [1, 2, 3, 4, 5] 출 력

if __name__ == "__main__":
    duplicate_breaker()



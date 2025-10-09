# Q1 조건문의 참과 거짓
# 다음 코드의 결괏값은 무엇일까?
# a = "Life is too short, you need python"
# if "wife" in a: print("wife")
# elif "python" in a and "you" not in a: print("python")
# elif "shirt" not in a: print("shirt")
# elif "need" in a: print("need")
# else: print("none")

def one():
    a = "Life is too short, you need python"
    if "wife" in a: print("wife")
    elif "python" in a and "you" not in a: print("python")
    elif "shirt" not in a: print("shirt") #이거
    elif "need" in a: print("need")
    else: print("none")

# Q2 3 의 배수의 합 구하기
# while 문을 사용해 1 부터 1000 까지의 자연수 중 3 의 배수의 합을 구해 보자.
# result = 0
# i = 1
# while i <= 1000:
# if <이 곳 을 완 성 하 세 요 >
# result += i
# i += 1
# print(result) # 166833 출 력

def two():
    result = 0
    i = 1
    while i <= 1000:
        if (i % 3 == 0): 
            result += i
        i += 1
    print(result) # 166833 출 력

def three():
    i = 0
    while True:
        i += 1
        if i>5:
            break
        print('*'*i)

def four():
    for i in range(1,101):
        print(i)

def five():
    scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
    total = 0
    for score in scores:
        total += score
    print(total//(len(scores)))

# 다음 소스 코드는 리스트의 요소 중에서 홀수만 골라 2 를 곱한 값을 result 리스트에 담는 예제이다.
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
# if n % 2 == 1:
# result.append(n*2)
# 이 코드를 리스트 컴프리헨션을 사용하여 표현해 보자.
def six():
    numbers = [1,2,3,4,5]
    result = [num for num in numbers if num % 2 == 1]
    print(result)


if __name__ == '__main__':
    six()
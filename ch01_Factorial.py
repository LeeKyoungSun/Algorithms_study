# 반복 구조의 팩토리얼 함수
def factorial_iter(n):
    result = 1
    for k in range(2, n+1) :
        result = result * k
    return result

# 순환 구조의 팩토리얼 함수
def factorial(n):
    if n ==1 :
        return 1 # n이 1이면 답을 알기 때문에 순환 호출을 멈춤
    else :
        return n * factorial(n-1) # 자신을 순환적으로 호출하는 부분, 문제의 크기는 작아져야함
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_iterative(n - 1)


print("반복문을 활용한 입력한 숫자까지의 곱의 합", factorial_iterative(5))
print("반복문을 활용한 입력한 숫자까지의 곱의 합", factorial_recursive(5))


# 두개의 자연수에 대한 최대공약수를 구하는 알고리즘 -> 최대 공약수 계산 (유클리드 호제법)
# A > B일때 A를 B로 나눈 나머지가 R, A,B의 최대공약수는 B와 R의 최대공약수와 같다
# GCD(192, 162)
# 192 162
# 162 30
# 30 12
# 12 6 ==> 6 위에 해당하는 나머지가 다 6으로 나누어떨어짐


def gcd(a, b):
    result = a % b
    if result == 0:
        return b
    return gcd(b, result)


print(gcd(192, 162))

# index

# [start_index : end_index]
#
exam_str_1 = '작은따옴표'
# print(exam_str_1[0:3])  # 작은따
# print(exam_str_1[-4:])  # 은따옴표 [:-4] -> 작 :-4 == :3 같다

# escape sequence
# print('hello \'tom\'')

# string format
# print(
#     "{age}세 개발자 {name}입니다.".format(age=33, name="live")
# )

# sep 는 분류기호(seperator)
demo = "312"
demo_2 = "set"
# print(demo_2, demo, sep='-')

# 10진수 형태로 입력받고 %X 로 출력시 16진수(hex) 대문자로 출력 %x는 소문자
a = 255
# print('%X' % a)  # FF

# 16진수 입력받고 %o로 출력시 8진수 변환
# ab = int('f', 16)
# print('%o' % ab)

# ord() 는 어떤 문자의 순서 위치(ordinal position) 값을 의미 (10진수 유니코드 값으로 변환)
# b = input()  # 영문자 입력 ex) A
# print(ord(b))
print('--------------------------')

# 단항의 연산자 기호인 -(negative)를 변수 앞에 붙일때 부호가 반대로 입력됌
exam_num_1 = -3
print(-exam_num_1)
print('--------------------------')

# 문자 연산
# ord는 문자의 순서를 10진수 유니코드 값으로 변환
# chr는 숫자를 문자로 변환
# exam_num_2 = ord(input()) + 1
# exam_num_3 = chr(exam_num_2)
# print(exam_num_3)
print('--------------------------')

# 소수 원하는 자리까지 자르기
# format(구하려는 수, 조건) '.2f' -> 소수 둘째자리
# demo_a = float(input())
# print(format(demo_a, '.2f'))

# print 가로로 출력
# end 옵션 "" 공백시 옆으로 붙어서 출력
# 콤마(,)로 구분하면, 문자, 숫자 상관없이 공백을 사이에 두고 출력
# print('variable',variable,end='')


# 비트 단위 시프트 ( 정수를 2배로 곱하거나 나누어 계산해주는 기능)
# 컴퓨터는 2진수 형태로 값을 저장하기 때문에 2진수 형태로 저장도어 있는 값들을 << >> 로 비트수만큼 계산하면 2배 or 1/2 로 됌
# 오른쪽 큰 표기 -> 2배, 왼쪽 큰 표기 2로 나누기
# 참고 파이썬에서는 실수값에 대한 계산은 되지 않음
print(10 << 1)  # 20
print(10 >> 1)  # 5

# a,b 입력받아 a를 2의 b제곱 출력
# a,b=map(int ,input().split())
# print(a * (2 ** b)) # (a << b) 와 같다


#삼항연산자
# a,b = map(int, input().split())
# print(True) if a < b else print(False)


#비트단위 연산자 ~
# 00000000 00000000 00000000 00000001 이고,
# ~1은 11111111 11111111 11111111 11111110 가 되는데 이는 -2를 의미
# print(~1) # 1을 32비트 2진수로 표현시 -2

# 이중 삼항연산자
# a,b,c = map(int, input().split())
# 3 -2 1
# result = (a if a < b else b) if ((a if a < b else b) < c) else c
# print(result)

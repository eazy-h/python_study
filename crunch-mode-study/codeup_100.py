# 6017
# str = input()
# new_str = str
# for i in range(3):
#     if i != 2:
#         new_str += " " + str
#
# print(new_str)


# 6081
# n = int(input(), 16)
# for i in range(1, 16):
#     print('%X' % n, '*', '%X' % i, '=%X' % (n * i), sep='')

# 6082
# n = int(input())
# result = ""
# for i in range(1, n + 1):
#     if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
#         result += "X"
#     else:
#         result += str(i)
#     if i != n:
#         result += " "
# print(result)

# 6083
# a, b, c = map(int, input().split())
# count = 0
# for i in range(a):
#     for j in range(b):
#         for k in range(c):
#             print(i, j, k)
#             count += 1
# print(count)

# 6084
# 녹음시간 s, 스테레오 c, bit b, hz h
# h, b, c, s = map(int, input().split())
# result = (h * b * c * s) / 8 / 1024 / 1024
# print(format(result, '.1f'), 'MB')


# 6086
# a = int(input())
# sum = 0
# for i in range(1, a + 1):
#     sum += i  #
#     if sum >= a:
#         print(sum)
#         break


# 6087
# n = int(input())
# for i in range(1, n + 1):
#     if i % 3 == 0:
#         continue
#     print(i, end=' ')

# 6088 (등차 같은 수열 -> 차이가 같은 수의 나열)
# a 시작값, b 등차값, c 몇번째 수를 알고 싶은지
# ex -> 1 3 5 입력시 -> 1 4 7 10 (13) 이 나와야함 13만 출력

# a, b, c = map(int, input().split())
# data_list = []
# i = 0
# while i < c:
#     data_list.append(a)
#     a += b
#     i += 1
# print(data_list[c - 1])

# a, b, c = map(int, input().split())
# total = a
# for _ in range(c-1):
#     total = total + b
# print(total)

# 6089 (등차 같은 수열 -> 차이가 같은 수의 나열)
# a, r, n = map(int, input().split())
# total = a
# for _ in range(n-1):
#     total *= r
# print(total)

# 6090 (시작:a, 곱할값:m, 더할값:d, 몇번째수:n)
# a, m, d, n = map(int, input().split())
# result = a
# for _ in range(n - 1):
#     result = (result * m) + d
#
# print(result)


# 6091 (겹치는 날짜 구하기)

# 3 6 9 12 15 18 21
# 14 21 28 35 42 49 56 63
# 27 36 45
# a, b, c = map(int, input().split())
# day = 1
# # day에 각 출석일이 나누어 떨어지지 않으면 계속 day추가하기
# while day % a != 0 or day % b != 0 or day % c != 0:
#     day += 1
# print(day)

# 6092 1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.
# 출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

n = int(input())  # 불린 횟수
a = input().split()  # 픽한 번호들

for i in range(n):
    a[i] = int(a[i])

tmp_list = [0] * 23

for i in range(n):
    tmp_list[a[i]-1] += 1

for data in tmp_list:
    print(data, end=' ')

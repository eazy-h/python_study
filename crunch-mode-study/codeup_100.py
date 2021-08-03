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
h, b, c, s = map(int, input().split())
result = (h * b * c * s) / 8 / 1024 / 1024
print(format(result, '.1f'), 'MB')

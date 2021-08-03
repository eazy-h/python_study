# Quiz 1.
# 1~10000까지의 8이 들어가는 숫자 갯수 찾기
count = 0

for i in range(1, 10000):
    for j in str(i):  # 8080 -> 4번 for문
        if j == '8':
            count = count + 1

# print(count)

# Quiz 2.
# 구구단 2단
# for i in range(1, 10):
#     print(
#         "{0} * {1} = {2}".format(2, i, 2 * i)
#     )

# Quiz 3.
# 구구단 모두 출력 1~9
# for i in range(2, 10):
#     print(i, "단")
#     for j in range(1, 10):
#         print(
#             "{} * {} = {}".format(i, j, i * j)
#         )

# a, b, c =map(int,input().split())
# plus_no = a+b+c
# avg_no = plus_no / 3
# print(plus_no, format(avg_no, '.2f'))


# Quiz 4.
# 월 숫자 입력시 계절 출력
# a = int(input())
# w = [12, 1, 2]
# sp = [3, 4, 5]
# sm = [6, 7, 8]
# f = [9, 10, 11]
# if a in w:
#     print("winter")
# elif a in sp:
#     print("spring")
# elif a in sm:
#     print("summer")
# else:
#     print("fall")

# a=int(input())
# if a//3==1:
#     print('spring')
# elif a//3==2:
#     print('summer')
# elif a//3==3:
#     print('fall')
# else:
#     print('winter')


# Quiz. 5

# a부터 입력한 문자까지 순서대로 공백 두고 한줄 출력
# ex) d -> a b c d

# a = ord(input())
# b = ord('a')
#
# while b <= a:
# 	print(chr(b), end="" if b == a else " ")
# 	b+=1
#


# Quiz. 6
# 입력받은 숫자를 1부터 더했을때 몇번째 index 까지의 합인지 마지막 index 구하기
# num = int(input())
# sum = 0
# for i in range(1, num + 1):
#     sum += i
#     if sum >= num:
#         print(i)
#         break
#
# # Quiz. 7
# # 주사위 n, m 숫자를 입력받고 나올 수 있는 경우의 수를 출력
# # ex) 2 2 -> 1 1 / 2 1 / 1 2 / 2 2
# a, b = map(int, input().split())
# for i in range(1, a+1):
#     for j in range(1, b + 1):
#         print(i, j)


n = input()

for i in range(1, 10):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

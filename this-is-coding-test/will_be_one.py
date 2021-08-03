#그리디
# 1이 될때까지 아래의 연산을 반복하되 최소한의 연산 횟수 구하기
# 입력된 값 n에서 -1
# n을 k로 나눈다

# 내가 푼 방법
n, k = map(int, input().split())
count = 0
while n > 1:
    if n % 5 != 0:
        n -= 1
        count += 1
    else:
        n = n // k
        count += 1

print(count)


# 교재 방법
# n, k = map(int, input().split())  # N, K값 입력
# count = 0
# while True:
#     target = (n // k) * k  # target = 나누어 0으로 떨어지는 수로 만들기 (k의 배수)
#     count += (n - target)  # 여기서 나머지가 1이면 count + 1 0이면 count 0
#     n = target  # n을 타겟으로 변경 즉 위에 코드에서 -1 했다고 봐도 무방
#     if n < k:
#         break
#     n //= k  # target으로 만들어놓고 나누기
#     count += 1  # count + 1
#
# count += (n - 1)  # 마지막으로 남은 수 -1씩
#
# print(count)
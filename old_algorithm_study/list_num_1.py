import time

# 1이 될때까지 반복
# 어떤 수 N이 1이 될떄까지 아래와 같이 2개중 하나를 반복적으로 선택해 수행하려 한다.
# 1. N - 1,
# 2. N / K (조건 - N이 K로 나누어 0이 될때만 연산하기)
# ex) N = 17 / K = 4일때 2번 조건이 되지 않으므로 1번 먼저 하고 16 % 4 = 0이기에 나누기 연산
# 위처럼 연산을 반복하여 N이 결국 1로 되어지는 최소한의 횟수를 구하기
# 입력조건  1 <= N <= 100,000 / 2 <= K <= 100,000
n, k = map(int, input().split())

start_time = time.time()
count = 0
while True:
    if n == 1:
        break
    elif n % k == 0:
        n //= k
        count = count + 1
    else:
        n = n - 1
        count = count + 1

end_time = time.time()
#
print(count)  # 6분
print("%f초 걸렸습니다." % (end_time - start_time))

# 6
# 0.000007초 걸렸습니다.

n_2, k_2 = map(int, input().split())
# 예제코드
exam_start_time = time.time()
exam_count = 0
while True:
    target = (n_2 // k_2) * k_2  # target = 나누어 0으로 떨어지는 수로 만들기 (k의 배수)
    exam_count += (n_2 - target)  # 여기서 나머지가 1이면 count + 1 0이면 count 0
    n_2 = target  # n_2를 타겟으로 변경 즉 위에 코드에서 -1 했다고 봐도 무방
    if n_2 < k_2:
        break
    n_2 //= k_2  # target으로 만들어놓고 나누기
    exam_count += 1  # count + 1

exam_end_time = time.time()
exam_count += (n_2 - 1)  # 마지막으로 남은 수 -1씩
print(exam_count)
print("%f초 걸렸습니다." % (exam_end_time - exam_start_time))

# 6
# 0.000008초 걸렸습니다.

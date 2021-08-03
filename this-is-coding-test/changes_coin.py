#그리디
import time

# 거스름돈 최소로 거슬러주기
n = 1260
count = 0
coin_array = [500, 100, 50, 10]

start_time = time.time()

# for coin in coin_array:
#     count += n // coin  # 거스름돈으로 각 동전별 거슬러줄 수 있는 개수 세기
#     n = n % coin  # 해당 금액을 현재 동전으로 거스르고 남은 돈


for coin in coin_array:
    count += n // coin
    n = n % coin
print(count)

end_time = time.time()

# print(f"소요시간 : {end_time - start_time}")
# print(f"거슬러줘야 할 동전의 수는 {count}개")  # 7분

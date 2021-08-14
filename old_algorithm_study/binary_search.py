import time


# item = 찾는 데이터
# 최소값과 최대값의 인덱스를 지정한다.
# 주어진 배열의 길이만큼 반복하며 중간 인덱스의 값을 guess 변수로 활용한다.
# 짐작하는 guess의 값이 item값보다 작으면 최소값의 인덱스를 guess의 인덱스에 +1 해준다.(mid + 1)
# 짐작하는 guess의 값이 item값보다 크면 최대값의 인덱스를 guess의 인덱스에 -1 해준다.(mid - 1)
# 반복하면서 guess의 값과 item값이 일치할 때 return mid, 리스트에 없는 숫자를 입력한다면 return None


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1

    return None


# 성능 측정 시작
start_time = time.time()

num_list = [1, 11, 32, 64]
print(binary_search(num_list, 64))

# 성능 측정 종료
end_time = time.time()

print('소요시간:', end_time - start_time)

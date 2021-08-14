# 퀵 정렬

# 정렬중 가장 많이 사용되는 알고리즘 (병합정렬과 속도 비슷)
# 기준 데이터를 임의로 지정 후 그 기준보다 큰 데이터와 작은 데이터의 위치를 swap
# 기준 데이터는 pivot, 대부분 프로그래밍 언어의 정렬은 퀵정렬
# 첫번째 데이터를 pivot으로 설정 후 왼쪽(start)에서 pivot보다 큰 수를, 오른쪽 끝(end)에서 pivot보다 작은수를 찾아서 서로의 위치를 교환
# 이때 start와 end가 교차된다면 end와 pivot을 서로 교환하여 분할한다 (좌 pivot 우) 이후 반복
# 시간복잡도 O(NlogN) but 이미 데이터가 정렬되어 있다면 매우 느림 (삽입정렬은 거의 정렬되어 있을시 빠름)


arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:  # 오른쪽 수가 더 클때까지 즉, 정렬이 될떄까지 반복
        # 좌측에서 찾는 반복 (pivot보다 큰 수 찾기)
        # pivot = 5
        # 1이 9까지만 가야함 and pivot이 left 더 크면 left가 큰 숫자를 찾을때까지 오른쪽(+1)으로 이동
        while left <= end and arr[pivot] >= arr[left]:
            left += 1

        # 우측에서 찾는 반복 (pivot보다 작은 수 찾기)
        # 9가 1까지만 와야함 and right가 pivot보다 더 크면 더 작은 수를 찾을때까지 왼쪽(-1)으로 이동
        while right > start and arr[pivot] <= arr[right]:
            right -= 1

        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right - 1)  # swap 한 pivot 기준 start=start, end=right-1
    quick_sort(arr, right + 1, end)  # swap 한 pivot 기준 start=right+1, end=end


quick_sort(arr, 0, len(arr) - 1)

print(arr)

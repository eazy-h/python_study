# 선택 정렬

# 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 변경
# 매번 가장 작은 데이터를 선택
# 주어진 값의 길이 전체를 확인 후 가장 작은 데이터를 찾아서 맨 앞으로 이동
# 데이터를 앞으로 보내는 과정은 n-1번 반복  3개의 수가 주어지면 최대 2번
# 2중 for문 시간복잡도 O(N2)

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(arr) - 1):  # n-1번 반복해야하기 때문 -1해줘도 되고 안해줘도 됌
    print(i, end=", ")
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    temp = arr[i]  # 변경해야할 앞에 i 인덱스 데이터 temp 잠시 넣기
    arr[i] = arr[min_index]  # 0번 인덱스엔 min_index가 들어가야함
    arr[min_index] = temp  # 가장 작은 수가 있던 index에 temp 값 할당
    # arr[i], arr[min_index] = arr[min_index], arr[i]  위 코드 3줄과 같은 의미 swap

print(arr)

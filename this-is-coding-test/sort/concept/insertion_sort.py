# 삽입 정렬
# 데이터를 하나씩 확인 후 적절한(어떤 기준점의 좌 or 우) 위치에 삽입
# 선택정렬에 비해 실행 시간 측면으로 조금 효율적
# 왼쪽은 이미 정렬되어 있다는 가정하에 접근


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 5, 7 -> 9
for i in range(len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]:
            temp = arr[j - 1]  # 큰 값을 temp에 넣기
            arr[j - 1] = arr[j]  # 큰 값이 있던 위치에 작은 값 넣기
            arr[j] = temp  # 작은 값이 있던 위치에 큰 값 temp 넣기
            # arr[j], arr[j - 1] = arr[j - 1], arr[j]

        else:  # 1,2,3,4 에서 5를 만났을때 4와 비교시 이미 크다면 1,2,3은 확인하지 않도록 break
            break

print(arr)

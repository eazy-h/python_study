import time

# def solution(nums):
#     # 중복제거 후 리스트로 받기
#     result_set = list(set(nums))
#     result_count = len(result_set)  # 선택할 수 있는 갯수
#     choice_count = len(nums) // 2  # 뽑을 수 있는 갯수
#     if choice_count < result_count:  # 3(choice) < 4 면 무적권 choice갯수만큼만 가져가야함
#         return choice_count
#     else:
#         return result_count  # 반대로 뽑을 수 있는 갯수가 중복제거한 선택할 수 있는 갯수보다 크면 선택 가능한만큼만 (중복제거)
#
#
# print(solution([3, 3, 3, 2, 2, 2]))


# 2번
# [5][5] == 0, 0
# def solution(dirs):
#     init_map = []
#     x = 0
#     y = 0
#     str_set = list(dirs)
#     count = 0
#     overlap_count = 0
#     for i in range(len(str_set)):
#         if x < -5 or y < -5 or x > 5 or y > 5:
#             continue
#         # if i != 0:
#         init_map.append(list(map(int, (x, y))))
#         if str_set[i] == 'U':
#             x = x - 1
#         elif str_set[i] == 'D':
#             x = x + 1
#         elif str_set[i] == 'L':
#             y = y - 1
#         elif str_set[i] == 'R':
#             y = y + 1
#         if [x, y] in init_map:
#             count += 1
#             if count > 1:
#                 origin_index = init_map.index([x, y])
#                 if init_map[origin_index] == [x, y]:
#                     overlap_count += 1
#
#     coordinate = []
#     for i in range(len(init_map)):
#         coordinate.append(init_map[i])
#     return len(coordinate) - overlap_count

# print(solution("LULLLLLLU"))

start_time = time.time()

# 3번
# def solution(a, b):
#     count = 0
#     b.sort()  # B팀의 리스트를 오름차순 정렬
#     for i in range(len(a)):
#         for j in range(len(b)):
#             if b[j] > a[i]:  # 두개의 배열의 데이터 비교
#                 count += 1  # 이긴 경우 count + 1
#                 del b[j]  # 해당 배열은 이제 돌 필요가 없으니 제거
#                 break  # b배열 반복 break
#     return count
#
#
# print(solution([20, 10, 4, 7, 3, 0, 21, 30, 30, 19], [40, 30, 30, 20, 10, 40, 100, 5, 0, 200, 8]))
# end_time = time.time()
#
# print(f"소요시간 :", format(end_time - start_time, '.5f'), "sec")

start_time = time.time()


def solution(a, b):
    # 계수정렬을 사용한 풀이
    demo_a = [0] * (max(a) + 1)
    demo_b = [0] * (max(b) + 1)
    # 각 주어진 a,b 배열의 값들의 인덱스로 0과 1로 배열 초기화
    for i in range(len(a)):
        demo_a[a[i]] += 1
    for i in range(len(b)):
        demo_b[b[i]] += 1
    count = 0

    print(demo_b)

    for i in range(len(demo_a)):
        for j in range(len(demo_b)):
            if demo_a[i] > 0 and demo_b[j] > 0:  # 주어진 a,b열의 해당 값이 1이상일때 (즉 값 비교가능시)
                if j > i:  # b배열의 index(실제론 주어진 데이터값)값이 더 클때
                    demo_b[j] -= 1  # 해당 배열은 다시 방문하지 않도록 0으로 초기화
                    count += 1  # +1
    return count


#
#
# print(solution([20, 10, 4, 7], [19, 3, 1, 0]))
print(solution([20, 10, 4, 7, 3, 0, 21, 30, 30, 19], [40, 30, 30, 20, 10, 40, 100, 5, 200, 8]))
# 구현부

end_time = time.time()
print(f"소요시간 :", format(end_time - start_time, '.5f'), "sec")
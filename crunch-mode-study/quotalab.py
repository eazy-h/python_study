# def solution(nums):
#     result_set = list(set(nums))
#     result_count = len(result_set)
#     choice_count = len(nums) // 2
#     if choice_count < result_count:
#         return choice_count
#     else:
#         return result_count
#
#
# print(solution([3, 3, 3, 2, 2, 2]))


# 2번
# [5][5] == 0, 0
def solution(dirs):
    init_map = []
    x = 0
    y = 0
    str_set = list(dirs)
    count = 0
    overlap_count = 0
    for i in range(len(str_set)):
        if x < -5 or y < -5 or x > 5 or y > 5:
            continue
        # if i != 0:
        init_map.append(list(map(int, (x, y))))
        if str_set[i] == 'U':
            x = x - 1
        elif str_set[i] == 'D':
            x = x + 1
        elif str_set[i] == 'L':
            y = y - 1
        elif str_set[i] == 'R':
            y = y + 1
        if [x, y] in init_map:
            count += 1
            if count > 1:
                origin_index = init_map.index([x, y])
                if init_map[origin_index] == [x, y]:
                    overlap_count += 1

    coordinate = []
    for i in range(len(init_map)):
        coordinate.append(init_map[i])
    return len(coordinate) - overlap_count


print(solution("LULLLLLLU"))

# 3번
# def solution(a, b):
#     b.sort()
#     count = 0
#     for i in range(len(a)):
#         for j in range(len(b)):
#             if b[j] > a[i]:
#                 count += 1
#                 del b[j]
#                 print(b)
#                 break
#     return count
#
#
# print(solution([5, 1, 3, 7], [2, 2, 6, 8]))

# def third(a_list=[], b_list=[]):
#     b_list.sort()
#     win_count = 0
#     for a in a_list:
#         for index, b in enumerate(b_list):
#             if b - a > 0:
#                 win_count += 1
#                 del b_list[index]
#                 break
#     return win_count
#
#
# print(third([5, 1, 3, 7], [2, 2, 6, 8]))

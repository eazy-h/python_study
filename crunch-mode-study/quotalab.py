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
    for i in range(len(str_set)):
        if x <= -5 or y <= -5 or x >= 5 or y >= 5:
            continue
        if str_set[i] == 'U':
            x = x - 1
        elif str_set[i] == 'D':
            init_map[x + 1][y] = 1
            x = x + 1
        elif str_set[i] == 'L':
            init_map[x][y - 1] = 1
            y = y - 1
        elif str_set[i] == 'R':
            init_map[x][y + 1] = 1
            y = y + 1
        init_map.append(list(map(int, (x, y))))

    # result = list(set(init_map))
    # print(len(init_map))
    count = 0
    demo_set = []
    demo2_set = []
    for i in range(len(init_map) - 1):
        for j in range(len(init_map[i])):
            # if i < 8:
            demo_set.append(init_map[i])
            demo2_set.append(init_map[i + 1])
                # print(init_map[i][j])
                # print(init_map[i + 1][j])
            # if list(init_map[i]) == list(init_map[i + 1]):
            #     print("con")
            # print()
        # print()
    return count


print(solution("ULURRDLLU"))

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

# index

# [start_index : end_index]
#
exam_str_1 = '작은따옴표'
print(exam_str_1[0:3])  # 작은따
print(exam_str_1[-4:])  # 은따옴표 [:-4] -> 작 :-4 == :3 같다


# escape sequence
print('hello \'tom\'')

# string format
print(
    "{age}세 개발자 {name}입니다.".format(age=33, name="live")
)

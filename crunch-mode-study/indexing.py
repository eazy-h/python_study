# 리스트 slice, remove(인자와 같은 첫번째 데이터를 찾아서 제거) del, pop(인자로 받은 인덱스 데이터를 제거)
a = [1, 2, 1, 3, 4, 5, 1]
b = [1, 2, 1, 3, 4, 5, 1]

a.remove(1)  # 가장 첫번째 조건에 부합하는 요소를 제거한다
# print(a)
# pop : 지워진 인덱스의 데이터값을 변수로 반환하지만, del은 반환하지 않음 -> del이 pop보다 수행속도가 미세하게 빠름
removed = b.pop(1)  # 인자는 지울 target index b에선 data=2를 말한다
# print(removed)  # 지워진 index 1의 데이터값
# print(b)

# 리스트에서 지울 리스트 비교해서 지우기
demo_a = [1, 2, 3, 4, 5, 6, 6, 7, 10]
remove_set = [5, 6, 10]

# 리스트 컴프리헨션 example => [ data for data in dat_set if data 조건문]
demo_list = [index for index in demo_a if index not in remove_set]  # 중복이 몇개건 다 제거
print(demo_list)
# result = [i for i in a if i not in remove_set]
# print(result)  # [1, 2, 3, 4, 7]


# 리스트 관련 메소드
demo_1 = [1, 3, 3, 23, 2, 3, 4, 4, 5]

# append - 원소 하나 삽입
demo_1.append(1244)
print(demo_1)

# sort 오름차순 정렬 반대는 reverse=True
demo_1.sort()
print(demo_1)

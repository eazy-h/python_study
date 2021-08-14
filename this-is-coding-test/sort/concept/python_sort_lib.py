# default sorted() 정렬 라이브러리 함수 (병합정렬, 최악의 시간복잡도 NlogN 보장)
# list, dic 정렬 가능


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 변수 반환 (key 매개변수 가능 -> 정렬 기준점)
# result = sorted(arr)
# print(result)

# 리스트 객체 내장 함수 sort() 바로 사용 (key 매개변수 가능 -> 정렬 기준점)
# arr.sort()
# print(arr)

# key를 이용한 정렬
array = [('바나나', 7), ('사과', 2), ('오렌지', 4)]


def key_setting(data):
    return data[1]


key_result = sorted(array, key=key_setting)
print(key_result)

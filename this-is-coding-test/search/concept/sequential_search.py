# 순차 탐색
# 리스트내에서 특정 데이터를 찾기 위해 순차적으로 데이터를 하나씩 확인하는 탐색
# 시간복잡도 O(N)

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1


print("생성할 원소의 갯수와 찾을 문자열을 한칸 띄고 순서대로 입력하세요.")
input_value = input().split()
n = int(input_value[0])
target = input_value[1]

print(f"띄어쓰기 1칸씩 구분하여 {n}개의 문자열을 입력하세요!!")
words = input().split()

print(sequential_search(n, target, words))

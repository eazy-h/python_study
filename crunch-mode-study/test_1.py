# n, k = map(int, input().split())  # N, K값 입력
# exam_count = 0
# while True:
#     target = (n // k) * k  # target = 나누어 0으로 떨어지는 수로 만들기 (k의 배수)
#     exam_count += (n - target)  # 여기서 나머지가 1이면 count + 1 0이면 count 0
#     n = target  # n을 타겟으로 변경 즉 위에 코드에서 -1 했다고 봐도 무방
#     if n < k:
#         break
#     n //= k  # target으로 만들어놓고 나누기
#     exam_count += 1  # count + 1
#
# exam_count += (n - 1)  # 마지막으로 남은 수 -1씩
#
# print(exam_count)

result = ''
while True:
    str = input()
    if str != 'q':
        result += str+"\n"
    else:
        result += str + "q"
        break

print(result)

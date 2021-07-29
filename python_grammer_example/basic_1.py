num = 1
str1 = "hello"

# 형변환
intValue = int('1')

# 타입검사
# print(type(intValue))

# 주석
"""
문자열도 가능하고 주석도 가능
"""

# 문자열
str2 = '작은따옴표'
str3 = '''줄바꿈
쌉가능
'''

# print(str3)
# 문자열을 문자로 변환 가능 [시작 인덱스:양수면 앞에서 갯수, 음수면 뒤에서 갯수]
print(str2[0:3])  # 작은따
print(str2[-4:])  # 은따옴표 [:-4] -> 작

# 이스케이프 시퀀스 \n \t \b  -> 특수문자 앞에 \
# print('안녕\t')
# print('하세요')
# print("Hello \"w\"")
print('hello \'tom\'')
#
# # 문자열 포맷(변환문자)
# # 사용 x
# oldIntroduce = '%d세이고 키는 %.1fcm입니다.' % (32, 184.4)
# print(oldIntroduce)
# # 추천 o
# newIntroduce = "{age}세이고 키는 {height}cm입니다.".format(age=32, height=184.4)
# print(newIntroduce)
#
# # 문자열 함수
# # 길이
# str4 = "eheheasdk dfsak"
# print("str4 길이 : ", len(str4))
# # 일치하는 수 반환
# print("a와 일치하는 갯수 : ", str4.count('a'))
# # 문자열 복사
# copy_str4 = str4[:-1]
# print("복사된 문자열 ", copy_str4)
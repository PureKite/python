# 너무 복잡하게 짠듯..!
# 문자열 입력받기
# s = input()
# s = sorted(s)  # ['1', '5', '7', 'A', 'B', 'C', 'K', 'K']

# # 모든 숫자를 더할 sum 변수 선언
# sum = 0
# n = -1
# # 리스트 숫자인 부분만 sum변수에 저장, 숫자 없으면 종료 // n을 통해 문자열 자를 부분 선언
# for i in range(len(s)):
#     if '0' <= s[i] and s[i] <= '9':
#         sum += int(s[i])
#         n = i
#     else:
#         break
# # n부터 자르기, sum 여부
# if sum > 0:
#     print(''.join(s[n+1:])+str(sum))
# else:
#     print(''.join(s[n+1:]))

# 답안 예시
data = input()
result = []
value = 0

# 문자 하나씩 확인
for x in data:
    # key point! isalpha() 함수가 중요했던 것 같다!
    if x.isalpha():  # 알파벳인 경우 결과 리스트에 삽입
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)
# 알파벳 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력
print(''.join(result))  # join을 이용하여 문자열로 출력

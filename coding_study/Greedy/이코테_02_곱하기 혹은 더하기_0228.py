s = list(map(int, input()))

s.sort(reverse=True)
result = s[0]
for i in range(1, len(s)):
    if s[i] > 1:
        result *= s[i]
    else:
        result += s[i]

print(result)


# python 예시코드
# data = input()
# result = int(data[0])

# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
# print(result)

# 예시가 훨씬 간단한 것 같다.
# 회의의 수
n = input()
# 회의의 정보
data = []
# for i in range(int(n)):
#     a, b = map(int, input().split())
#     data.append([a, b])
# data = sorted(data, key = lambda a:a[0])
# data = sorted(data, key = lambda a:a[1])

# result = 0
# count = 0

# for i, j in data:
#     if i >= result:
#         count += 1
#         result = j
# print(count)

# 더 간단한 버전
for i in range(int(n)):
    a, b = map(int, input().split())
    data.append((b, a))
data.sort()

result = 0
count = 0

for i in data:
    if i[1] >= result:
        count += 1
        result = i[0]
print(count)
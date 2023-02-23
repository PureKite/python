# 틀린 풀이!
# n, m = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]

# min_data = []
# for i in range(n):
#     min_data.append(min(data[i]))

# min_data = list(set(min_data))
# min_data.sort()

# if len(min_data) > 1:
#     print(min_data[1])
# else:
#     print(min_data[0])


# 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수 => 두 번째로 큰 수인지 알았는데 가장 큰 수였다..!
# 고쳐야 할 점 : 문제 파악 확실하게 할 것!

# 수정
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

min_data = []
for i in range(n):
    min_data.append(min(data[i]))

# min_data.sort()

print(max(min_data))
import heapq
# 배열의 크기
n = input()
data = []
for _ in range(int(n)):
    start, end = map(int, input().split())
    data.append((start, end))
## 이해가 필요..!
data.sort(key=lambda x: (x[0], x[1]))
result = [0]
for start, end in data:
    if start >= result[0]:
        heapq.heappushpop(result, end)
    else:
        heapq.heappush(result, end)
print(len(result))
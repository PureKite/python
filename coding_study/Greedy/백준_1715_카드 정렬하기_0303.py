import heapq
n = int(input())

data = []
for i in range(n):
    heapq.heappush(data, int(input()))

result = 0
if len(data) == 1:
    print(result)
else:
    while len(data) > 1:
        plus = heapq.heappop(data) + heapq.heappop(data)
        result += plus
        heapq.heappush(data, plus)
    print(result)
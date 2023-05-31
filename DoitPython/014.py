import sys
import heapq

input = sys.stdin.readline
n = int(input())
data = []
for _ in range(n):
    x = int(input())

    if x == 0:
        if data:
            print(heapq.heappop(data)[1])
        else:
            print(0)
    else:
        heapq.heappush(data, (abs(x), x))

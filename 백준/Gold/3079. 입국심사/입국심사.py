import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = []
for _ in range(n):
    num = int(input())
    data.append(num)

start = 1
end = max(data) * m
data.sort()
while start <= end:
    mid = (start+end) // 2
    total = 0
    for i in range(n):
        total += mid // data[i]
        if total > m:
            break
    if total < m:
        start = mid + 1
    else:
        end = mid - 1

print(start)
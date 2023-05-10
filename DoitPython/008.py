import sys

input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))

data.sort()
count = 0

for k in range(n):
    find = data[k]
    start = 0
    end = n - 1
    while start < end:
        if data[start] + data[end] == find:
            if start != k and end != k:
                count += 1
                break
            elif start == k:
                start += 1
            elif end == k:
                end -= 1
        elif data[start] + data[end] < find:
            start += 1
        else:
            end -= 1

print(count)

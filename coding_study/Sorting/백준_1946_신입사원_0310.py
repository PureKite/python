import sys
input = sys.stdin.readline
t = int(input())
count = []
for i in range(t):
    n = int(input())
    data = []
    for j in range(n):
        a, b = map(int, input().split())
        data.append((a, b))
    data = sorted(data, key=lambda x: x[0])
    min = data[0][1]
    cnt = 1
    for j in data:
        if min > j[1]:
            min = j[1]
            cnt += 1
    count.append(cnt)
for i in range(len(count)):
    print(count[i])

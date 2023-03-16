import sys
input = sys.stdin.readline
n = int(input())

data = []
for _ in range(n):
    num = list(map(int, input().split()))
    data.append(num)

for i in range(1, n):
    for j in range(len(data[i])):
        if j == 0:
            left = 0
        else:
            left = data[i-1][j-1]
        if j == len(data[i])-1:
            right = 0
        else:
            right = data[i-1][j]
        data[i][j] = data[i][j] + max(left, right)

print(max(data[n-1]))

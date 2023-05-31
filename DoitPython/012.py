import sys

input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
ans = [-1] * n
stack = []
for i in range(n):
    while stack and data[stack[-1]] < data[i]:
        ans[stack.pop()] = data[i]
    stack.append(i)

for i in ans:
    print(i, end=" ")

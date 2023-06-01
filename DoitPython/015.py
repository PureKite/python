import sys

input = sys.stdin.readline
n = int(input())
data = list(int(input()) for _ in range(n))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

for i in data:
    print(i)

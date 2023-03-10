import sys
input = sys.stdin.readline
n = int(input())
data = sorted(list(map(int, input().split())))
x = int(input())

cnt = 0
# 1, 2, 3, 5, 7, 9, 10, 11, 12
left, right = 0, n-1
while left < right:
    if data[left] + data[right] == x:
        cnt += 1
        left += 1
        right -= 1
    elif data[left] + data[right] < x:
        left += 1
    else:
        right -= 1
print(cnt)

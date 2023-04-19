# 1. start, end 값 정해주기
# 2. 이진탐색
# 3. 주의할 점 : 기준값보다 크면 기준값만큼만 더해준다.
import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
total = int(input())

start = 0
end = max(data)

while start <= end:
    s = 0
    mid = (start+end)//2
    for i in data:
        if i < mid:
            s += i
        else:
            s += mid
    if s > total:
        end = mid - 1
    else:
        start = mid + 1

print(end)

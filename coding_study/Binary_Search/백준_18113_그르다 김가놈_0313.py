import sys
input = sys.stdin.readline
# 김밥의 개수, 꼬다리의 길이, 김밥조각의 최소 개수
n, k, m = map(int, input().split())
array = []
for _ in range(n):
    kim = int(input())
    if kim > k * 2:
        array.append(kim-(2*k))
    elif kim - k > 0 and kim < 2 * k:
        array.append(kim-k)

if len(array) == 0:
    print(-1)
    exit(0)

result = -1
start, end = 1, max(array)
while start <= end:
    mid = (start+end) // 2
    total = sum([i // mid for i in array])

    if total < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
print(result)

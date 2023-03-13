n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)

sum = 0
data_max = data[0]
while True:
    if sum == m:
        print(data_max)
        break
    sum = 0
    data_max -= 1
    for i in data:
        if (i - data_max) > 0:
            sum += (i - data_max)
# 이진탐색
start = 0
end = max(data)

result = 0
while (start <= end):
    total = 0
    mid = (start+end) // 2
    for x in data:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)

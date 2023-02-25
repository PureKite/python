n = int(input())
data = list(map(int, input().split(' ')))

data.sort()

## 풀이 해석이 안됨..
target = 1
for x in data:
    if target < x:
        break
    target += x
print(target)
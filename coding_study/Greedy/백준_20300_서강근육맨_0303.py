n = input()
data = list(map(int, input().split()))

data.sort()
m = 0
if int(n) % 2 == 1:
    m = data.pop(-1)
result = [data[i] + data[-i-1] for i in range(len(data)//2)]
result.append(m)
print(max(result))
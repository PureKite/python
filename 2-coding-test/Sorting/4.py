n, k = map(int, input(). split())
data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))

data1.sort()
data2.sort(reverse=True)

for i in range(k):
    if data1[i] < data2[i]:
        data1[i], data2[i] = data2[i], data1[i]
    # else: break

s = 0
for i in data1:
    s += i
print(s)  # print(sum(data1))

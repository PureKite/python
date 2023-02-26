data = list(map(str, input().split('-')))

sum = []
for i in data:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    sum.append(cnt)
minus = sum[0]
for i in range(1, len(sum)):
    minus -= sum[i]
print(minus)
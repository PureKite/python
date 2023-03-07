n = int(input())
calendar = [0] * 366
final = 0

for _ in range(n):
    s, e = map(int, input().split())
    final = max(final, e)
    for i in range(s, e+1):
        calendar[i] += 1

row = 0
col = 0
ans = 0
for i in range(final+1):
    if calendar[i] != 0:
        row = max(row, calendar[i])
        col += 1
    else:
        ans += row * col
        row = 0
        col = 0

ans += row * col

print(ans)

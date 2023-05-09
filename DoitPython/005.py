# 내가 푼 풀이 => 시간초과
# 나머지 합 문제 핵심 아이디어를 잘 생각해야겠다
# => 특정 구간 수들의 나머지 연산을 더해 나머지 연산을 한 값과 이 구간 합의 나머지 연산을 한 값은 동일
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
s = [0] * n
c = [0] * m
s[0] = data[0]
count = 0
for i in range(1, n):
    s[i] = s[i - 1] + data[i]


for i in range(n):
    reminder = s[i] % m
    if reminder == 0:
        count += 1
    c[reminder] += 1

for i in range(m):
    if c[i] > 1:
        count += c[i] * (c[i] - 1) // 2

print(count)

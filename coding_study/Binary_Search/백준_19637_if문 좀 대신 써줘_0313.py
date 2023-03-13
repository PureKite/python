import sys
import bisect
input = sys.stdin.readline
n, m = map(int, input().split())
name = []
power = []
for _ in range(n):
    s, p = input().split()
    name.append(s)
    power.append(int(p))
for _ in range(m):
    p = int(input())
    index = bisect.bisect_left(power, p)
    print(name[index])

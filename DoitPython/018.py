import sys

input = sys.stdin.readline
s = list(map(int, input().rstrip()))

for i in range(len(s)):
    min_value = int(1e9)
    index = 0
    for j in range(len(s) - i):
        if min_value > s[j]:
            min_value = s[j]
            index = j
    s[len(s) - 1 - i], s[index] = s[index], s[len(s) - 1 - i]

print("".join(map(str, s)))

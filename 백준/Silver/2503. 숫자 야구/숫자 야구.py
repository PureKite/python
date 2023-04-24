import sys
from itertools import permutations
input = sys.stdin.readline

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
total = list(permutations(number, 3))
n = int(input())
for _ in range(n):
    num, s, b = map(int, input().split())
    num = list(str(num))
    removed = 0

    for i in range(len(total)):
        strike, ball = 0, 0
        i -= removed
        for j in range(3):
            if total[i][j] == num[j]:
                strike += 1
            elif num[j] in total[i]:
                ball += 1
        if strike != s or ball != b:
            total.remove(total[i])
            removed += 1
print(len(total))

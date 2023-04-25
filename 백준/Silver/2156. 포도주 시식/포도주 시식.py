import sys
input = sys.stdin.readline
n = int(input())

grape = list(int(input()) for _ in range(n))
dp = [0]*n
dp[0] = grape[0]

if n > 1:
    dp[1] = grape[0] + grape[1]
if n > 2:
    dp[2] = max(grape[2]+grape[1], grape[2]+grape[0], dp[1])

for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-3]+grape[i-1]+grape[i], dp[i-2]+grape[i])
print(dp[n-1])
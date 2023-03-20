n = int(input())
data = list(map(int, input().split()))
dp = [0] * n

count = 0
for i in range(1, n):
    for j in range(0, i):
        if data[i] > data[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp)+1)

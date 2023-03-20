n = int(input())

jump = [list(map(int, input().split())) for _ in range(n-1)]
k = int(input())

INF = 1e9
dp = [[INF, INF] for _ in range(n)]
dp[0][0] = 0

if n > 1:
    dp[1][0] = jump[0][0]
if n > 2:
    dp[2][0] = min(jump[0][0] + jump[1][0], jump[0][1])
if n > 3:
    for i in range(3, n):
        dp[i][0] = min(dp[i-1][0] + jump[i-1][0], dp[i-2][0] + jump[i-2][1])
        dp[i][1] = min(dp[i-1][1] + jump[i-1][0], dp[i-2]
                       [1] + jump[i-2][1], dp[i-3][0] + k)

print(min(dp[n-1][0], dp[n-1][1]))

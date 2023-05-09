# 조건까지는 맞았는데 점화식 부분이 살짝 틀렸다..ㅜ
# import sys
# input = sys.stdin.readline
# n = int(input())

# day = [0]
# cost = [0]
# for i in range(n):
#     t, p = map(int, input().split())
#     day.append(t)
#     cost.append(p)

# dp = [0] * (n+2)
# for i in range(1, n+1):
#     if i + day[i] <= n+1:
#         dp[i+day[i]] = max(dp[i+day[i]], dp[i]+cost[i], dp[i-1]+cost[i])
# print(max(dp))
import sys
input = sys.stdin.readline
n = int(input())

day = [0]
cost = [0]
for i in range(n):
    t, p = map(int, input().split())
    day.append(t)
    cost.append(p)

dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = max(dp[i], dp[i-1])  # 내가 생각한 점화식에서 추가하지 못했던 부분, 0일때 이전 값으로 넣어주기..!
    if i + day[i]-1 <= n:
        dp[i+day[i]-1] = max(dp[i+day[i]-1], dp[i-1]+cost[i])
print(max(dp))

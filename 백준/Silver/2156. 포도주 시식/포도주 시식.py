import sys
input = sys.stdin.readline
n = int(input())

grape = list(int(input()) for _ in range(n))

# 문제를 제대로 파악을 못함..
# max_value1 = 0
# max_value2 = 0
# max_value3 = 0

# if len(grape) < 3:
#     print(sum(grape))
# else:
#     if n % 3 == 0:
#         i = 0
#         while i < n:
#             max_value1 += grape[i] + grape[i+1]
#             max_value2 += grape[i+1]+grape[i+2]
#             max_value3 += grape[i]+grape[i+2]
#             i += 3
#         print(max(max_value1, max_value2, max_value3))
#     elif n % 3 == 1:
#         i = 0
#         while i < n-1:
#             max_value1 += grape[i] + grape[i+1]
#             max_value2 += grape[i+1] + grape[i+2]
#             max_value3 += grape[i] + grape[i+2]
#             i += 3
#         print(max(max_value1+grape[-1], max_value2, max_value3+grape[-1]))
#     else:
#         i = 0
#         while i < n - 2:
#             max_value1 += grape[i] + grape[i+1]
#             max_value2 += grape[i+1] + grape[i+2]
#             max_value3 += grape[i] + grape[i+2]
#             i += 3
#         print(max(max_value1+grape[-1]+grape[-2],
#               max_value2+grape[-2], max_value3+grape[-1]))

# https://hongcoding.tistory.com/48 참고
# 1. 현재 포도주와 이전 포도주를 마시고 전전 포도주는 마시지 않음(grape[i]+grape[i-1]+dp[i-3])
# 2. 현재 포도주와 전전 포도주를 마시고 이전 포도주는 마시지 않음(grape[i]+dp[i-2])
# 3. 현재 포도주를 마시지 않음(dp[i-1])

# 점화식을 세워볼 것!
# 
dp = [0]*n
dp[0] = grape[0]

if n > 1:
    dp[1] = grape[0] + grape[1]
if n > 2:
    dp[2] = max(grape[2]+grape[1], grape[2]+grape[0], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-3]+grape[i-1]+grape[i], dp[i-2]+grape[i])

print(dp[n-1])

# 예제랑 찾아본 반례들은 맞았는데 어디서 틀린지 모르겠다... => [0][1]로 구분해줬어야하는데 구분을 안해줘서 틀린 것 같다.

# import sys
# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#     n = int(input())

#     data = list(list(map(int, input().split())) for _ in range(2))

#     dp = [0]*n

#     zero_start = data[0][0]
#     one_start = data[1][0]

#     dp[0] = max(zero_start, one_start)

#     if n >= 2:
#         zero_start += data[1][1]
#         one_start += data[0][1]
#         dp[1] = max(zero_start, one_start)

#     d1 = 0
#     d2 = 0
#     if n >= 3:
#         zero_start += data[0][2]
#         one_start += data[1][2]
#         dp[2] = max(zero_start, one_start, dp[0] +
#                     max(data[0][2], data[1][2]))
#     if n >= 4:
#         for i in range(3, n):
#             if i % 2 == 0:
#                 zero_start += data[0][i]
#                 one_start += data[1][i]
#             else:
#                 zero_start += data[1][i]
#                 one_start += data[0][i]

#             dp[i] = max(zero_start, one_start, dp[i-2] +
#                         max(data[0][i], data[1][i]), d1 + data[1][i], d2 + data[0][i])
#     print(dp[n-1])

# # 점화식 좀 더 생각해보기
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    data = list(list(map(int, input().split())) for _ in range(2))

    if n > 1:
        data[0][1] += data[1][0]
        data[1][1] += data[0][0]

    if n > 2:
        for j in range(2, n):
            data[0][j] += max(data[1][j-1], data[1][j-2])
            data[1][j] += max(data[0][j-1], data[0][j-2])
    print(max(data[0][n-1], data[1][n-1]))

# 항상 오른쪽으로만 이동가능하다.
# i번째 돌에서  j(i < j)번째 돌로 이동할 때 (j - i) × (1 + |Ai - Aj|) 만큼 힘을 쓴다.
# 돌을 한번 건너갈 때마다 쓸 수 있는 힘은 최대 K이다.

# 이진탐색으로 푼 풀이..
import sys
# input = sys.stdin.readline


# def binary_search(start, end):
#     while (start <= end):
#         mid = (start + end) // 2
#         visited = [False] * (n + 1)  # 밟은
#         visited[1] = True
#         for i in range(1, n+1):
#             if (visited[-1]):  # 마지막 도달
#                 break
#             if (visited[i]):
#                 for j in range(i+1, n+1):
#                     power = (j-i) * (1 + abs(arr[j] - arr[i]))
#                     if (power < mid):
#                         visited[j] = True
#         if (visited[-1]):  # 징검다리 도착 -> mid 값 작아지도록
#             end = mid - 1
#         else:
#             start = mid + 1
#     return end


# n = int(input())
# arr = list(map(int, input().split()))
# arr = [0] + arr

# print(binary_search(0, 1000000))

# dp로 풀었을 때
n = int(sys.stdin.readline())
stones = list(map(int, sys.stdin.readline().split()))
INF = 1e9
# dp = [INF for _ in range(n)]
dp = [0] + [INF] * (n - 1)  # 0, 1e9, 1e9, 1e9

# (0 -> 1), (0 -> 2), (1 -> 2), (0 -> 3), (1 -> 3) 등등등
for i in range(1, n):
    for j in range(0, i):
        # (j - i) × (1 + |Ai - Aj|)
        power = max((i - j) * (1 + abs(stones[i] - stones[j])), dp[j])
        # 1 -3 : 2, 3 -5 : 2
        dp[i] = min(dp[i], power)
print(dp[n - 1])


# 시간 초안에 푼 풀이... 근데 왜 통과인건지를 모르겠음..ㅠ..
n = int(input())

stone = list(map(int, input().split()))

dp = [0] * n

for i in range(1, n):
    min_k = 1e9
    max_k = []
    for j in range(0, i):
        max_k.append(max(dp[j], ((i-j) * (1 + abs(stone[j]-stone[i])))))
    dp[i] = min(max_k)

print(dp[-1])

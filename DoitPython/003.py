import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 합 구하기
sum = [0] * (n+1)
sum[1] = data[0]
for i in range(2, n+1):
    sum[i] = sum[i-1] + data[i-1]
# 구간 합
p = []
for _ in range(m):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])

input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0
for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)
for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])

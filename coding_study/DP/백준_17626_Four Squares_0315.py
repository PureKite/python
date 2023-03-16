# 시간 초과
import math

n = int(input())
dp = [0, 1]

for i in range(2, n+1):
    minValue = 4
    for j in range(1, int(math.sqrt(i)) + 1):
        minValue = min(minValue, dp[i - j**2])
    dp.append(minValue + 1)

print(dp[n])


# 브루트포스로 풀어야 시간초과가 없음..
def fourSquares(n):
    # √n이 정수일 때
    if int(math.sqrt(n)) == math.sqrt(n):
        return 1
    # √(n - i^2)이 정수일 때
    for i in range(1, int(math.sqrt(n)) + 1):
        if int(math.sqrt(n - i**2)) == math.sqrt(n - i**2):
            return 2
    # √(n - i^2 - j^2)이 정수일 때
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - i**2)) + 1):
            if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(n - i**2 - j**2):
                return 3
    # 남은 경우는 4
    return 4


n = int(input())
print(fourSquares(n))

# 출처 : https://kau-algorithm.tistory.com/564

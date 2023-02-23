# N, K 입력
n, k = map(int, input().split())

count = 0
while n > 1:
    if n % k == 0:
        n /= k # N을 K로 나누기
    else:
        n -= 1 # N에서 1 빼기
    count += 1
print(count) # 최종 출력


# 최대한 많이 나누기
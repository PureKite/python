# N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k

# 마자막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
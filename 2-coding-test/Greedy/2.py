n, m, k = map(int, input().split(' '))
num = list(map(int, input().split(' ')))

start_time = time.time()
num.sort(reverse=True)

sum = 0
for i in range(m):
    if (i+1) % k == 0:
        sum += num[1]
    else:
        sum += num[0]

print(sum)
# 가장 큰 수와 두 번째로 큰 수만 저장
# 즉, 가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산을 반복
# 반복되는 수열에 대해 파악
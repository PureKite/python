n = int(input())
start = 1
end = 1
count = 1
s = 1
while end != n:
    if s < n:
        end += 1
        s += end
    elif s == n:
        count += 1
        end += 1
        s += end
    else:
        s -= start
        start += 1
print(count)

# 빠른 풀이
n = int(input())
answer = 0
cnt = 1
while n > 0:
    if n % cnt == 0:
        answer += 1
    n -= cnt
    cnt += 1
print(answer)

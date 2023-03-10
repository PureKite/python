n, l = map(int, input().split())
pipe = list(map(int, input().split()))

pipe.sort()

start = 0
cnt = 0
for p in pipe:
    if start < p:
        # p + l -1(0.5+0.5)
        start = p + l - 1
        cnt += 1
print(cnt)

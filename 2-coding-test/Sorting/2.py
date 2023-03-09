n = int(input())
data = [int(input()) for _ in range(n)]
data.sort(reverse=True)
# data = sorted(data, reverse = True)
for i in data:
    print(i, end=' ')

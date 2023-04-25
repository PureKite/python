import sys
input = sys.stdin.readline
n, k = map(int, input().split())

start = 0
end = n

while start <= end:
    mid = (start + end) // 2
    s = (mid+1) * (n-mid+1)

    if k < s:
        end = mid - 1
    elif k == s:
        print('YES')
        sys.exit(0)
    else:
        start = mid + 1
print('NO')

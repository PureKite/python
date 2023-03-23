# 팀 합치기 => union_parent
# 같은 팀 여부 확인 => find_parent

n, m = map(int, input().split())


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union_parent(parent, b, c)
    else:
        if find_parent(parent, b) != find_parent(parent, c):
            print("NO")
        else:
            print("YES")

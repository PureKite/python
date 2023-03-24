import sys
input = sys.stdin.readline
# 루트 노드 찾기


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 합집합 노드


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 탐승구 수 G 입력
g = int(input())
# 비행기 수 P 입력
p = int(input())

parent = [0] * (g+1)

for i in range(1, g+1):
    parent[i] = i

count = 0
for i in range(p):
    info = find_parent(parent, int(input()))
    if info == 0:
        break
    union_parent(parent, info, info - 1)
    count += 1
print(count)

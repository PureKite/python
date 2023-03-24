# 여행지의 수 n, 여행 계획에 속한 도시의 수 m 입력받기
# n X m 행렬 입력받기
# 도로는 양방향

# find_parent, union_parent 사용하면 되는 듯!
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


n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

data = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            union_parent(parent, i+1, j+1)

plan = list(map(int, input().split()))
result = find_parent(parent, plan[0])
flag = False
for i in plan:
    if result == find_parent(parent, i):
        flag = True
    else:
        flag = False
if flag == True:
    print("YES")
else:
    print("NO")

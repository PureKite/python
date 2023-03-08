n = int(input())
v = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(v):
    x, y = map(int, input().split())
    # 서로 연결되어 있는 정보 => 양방향..?
    graph[x].append(y)
    graph[y].append(x)

count = 0

# 전형적인 dfs문제


def dfs(graph, start, visited):
    global count
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)


dfs(graph, 1, visited)
print(count)

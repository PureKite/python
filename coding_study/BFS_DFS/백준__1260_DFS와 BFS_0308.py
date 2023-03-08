from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(n):
    visited[n] = True
    print(n, end=' ')

    graph[n].sort()
    for i in graph[n]:
        if not visited[i]:
            dfs(i)


def bfs(n):
    queue = deque([n])
    visited[n] = True
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        graph[now].sort()
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(v)
visited = [False] * (n+1)
print()
bfs(v)

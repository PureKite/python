import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, start, visited):
    for i in graph[start]:
        if visited[i] == -1:
            visited[i] = start
            dfs(graph, i, visited)


dfs(graph, 1, visited)
for i in range(2, n+1):
    print(visited[i])

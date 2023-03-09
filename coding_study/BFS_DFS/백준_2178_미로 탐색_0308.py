from collections import deque
n, m = map(int, input().split())

data = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if data[nx][ny] == 1:
                    data[nx][ny] = data[x][y] + 1
                    queue.append((nx, ny))


bfs(0, 0)
print(data[n-1][m-1])

# bfs까지 생각은 했는데 못풀었다..
# import sys
# from collections import deque
# input = sys.stdin.readline

# n, l, r = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]


# dx = [0, 1]
# dy = [1, 0]


# def bfs(x, y):
#     queue = deque((x, y))

#     while queue:
#         nx, ny = queue.popleft()
#         print(nx, ny)
#         for i in range(2):
#             nnx = nx + dx[i]
#             nny = ny + dx[i]
#             if nnx < 0 or nnx > n or nny < 0 or nny >= n:
#                 break
#             if l <= abs(data[nnx][nny] - data[nx][ny]) <= :
#                 queue.append((nnx, nny))
import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0


def process(x, y, index):
    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))
    union[x][y] = index
    summary = graph[x][y]
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    for i, j in united:
        graph[i][j] = summary // count
    return count


total_count = 0
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if index == n * n:
        break
    total_count += 1
print(total_count)


# 참고 : https://ryu-e.tistory.com/40, https://yuna0125.tistory.com/m/176
# - 인구 이동이 없을 때까지 반복
# - 모든 것을 bfs로 방문하여 연합 진행
#   - 인접 국가를 탐색하면서 인구 차이 l명 이상, r명 이하인 경우 연합 진행
#   - 연합 국가 간 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 되도록 계산
# - 지금까지 인구 이동이 없는 경우 그만

n, l, r = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    queue = deque()
    union = []
    queue.append((i, j))
    union.append((i, j))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(A[nx][ny] - A[x][y]) <= r:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union.append((nx, ny))
    return union


result = 0
while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)

                if len(country) > 1:
                    flag = 1
                    people = sum(A[x][y] for x, y in country) // len(country)

                    for x, y in country:
                        A[x][y] = people

    if flag == 0:
        print(result)
        break

    result += 1

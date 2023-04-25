# 모든 구름이 di 방향으로 si칸 이동한다.
# 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
# 구름이 모두 사라진다.
# 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
# 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
# 예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
# 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
import sys
# from collections import deque
# input = sys.stdin.readline
# n, m = map(int, input().split())
# graph = list(list(map(int, input().split())) for _ in range(n))

# q = deque()

# for _ in range(m):
#     s, d = map(int, input().split())
#     q.append((s, d))
# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, -1, -1, -1, 0, 1, 1, 1]
# p_x = [-1, 1, -1, 1]
# p_y = [-1, -1, 1, 1]

# while q:
#     s, d = q.popleft()
#     x, y = 0, n-2
#     nx = (x + (dx[s-1]*d)) % n
#     ny = (y + (dy[s-1]*d)) % n
#     x1, x2, y1, y2 = nx % n, (nx+1) % n, ny % n, (ny+1) % n
#     graph[y1][x1] += 1
#     graph[y1][x2] += 1
#     graph[y2][x1] += 1
#     graph[y2][x2] += 1

#     count = 0
#     for i in range(4):
#         ny1 = y1 + p_y[i]
#         nx1 = x1 + p_x[i]
#         if ny1 >= n or ny1 < 0 or nx1 >= n or nx1 < 0:
#             continue
#         if graph[ny1][nx1] > 0:
#             count += 1
#     graph[y1][x1] += count

#     count = 0
#     for i in range(4):
#         ny1 = y1 + p_y[i]
#         nx2 = x2 + p_x[i]
#         if ny1 >= n or ny1 < 0 or nx2 >= n or nx2 < 0:
#             continue
#         if graph[ny1][nx2] > 0:
#             count += 1
#     graph[y1][x2] += count

#     count = 0
#     for i in range(4):
#         ny2 = y2 + p_y[i]
#         nx1 = x1 + p_x[i]
#         if ny2 >= n or ny2 < 0 or nx1 >= n or nx1 < 0:
#             continue
#         if graph[ny2][nx1] > 0:
#             count += 1
#     graph[y2][x1] += count

#     count = 0
#     for i in range(4):
#         ny2 = y2 + p_y[i]
#         nx2 = x2 + p_x[i]
#         if ny2 >= n or ny2 < 0 or nx2 >= n or nx2 < 0:
#             continue
#         if graph[ny2][nx2] > 0:
#             count += 1
#     graph[y2][x2] += count

#     for i in range(n):
#         for j in range(n):
#             if (i == y1 or i == y2) and (j == x1 or j == x2):
#                 continue
#             else:
#                 if graph[i][j] >= 2:
#                     graph[i][j] -= 2

#     print(graph)

# 문제 이해를 잘 못함..!
# 구름이 계속 (n, 1), (n,2) (n-1, 1) (n-1, 2)로 초기화되는줄 알았다
# 꼭 다시 풀어보기!!!!

# 참고 : https://resilient-923.tistory.com/193
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
move_list = []
for i in range(m):
    temp = list(map(int, input().split()))
    move_list.append([temp[0]-1, temp[1]])

clouds = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
for i in range(m):
    x, y = move_list[i]
    # 1.이동한구름위치
    nextcloud = []
    for cloud in clouds:
        nx = (cloud[0] + dx[x] * y) % n
        ny = (cloud[1] + dy[x] * y) % n
        nextcloud.append([nx, ny])
    # 방문처리
    visited = [[0]*n for _ in range(n)]
    for cloud in nextcloud:
        # 지금 칸에 비를 뿌린다.
        A[cloud[0]][cloud[1]] += 1
        visited[cloud[0]][cloud[1]] = 1
    # 3.구름이 모두사라진다
    clouds = []

    # 물복사버그 대각선으로 퍼진다
    dx2 = [-1, -1, 1, 1]
    dy2 = [-1, 1, -1, 1]
    for _x, _y in nextcloud:
        cnt = 0
        for i in range(4):
            nx = _x + dx2[i]
            ny = _y + dy2[i]
            if 0 <= nx < n and 0 <= ny < n and A[nx][ny]:  # 물이 있을 때
                cnt += 1
        A[_x][_y] += cnt
    # 4. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    for i in range(n):
        for j in range(n):
            if A[i][j] >= 2 and visited[i][j] == 0:
                A[i][j] -= 2
                clouds.append([i, j])
total = 0
for i in range(n):
    total += sum(A[i])
print(total)

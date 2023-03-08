from collections import deque
# r, c, n 입력
r, c, n = map(int, input().split())

# 주어진 폭탄 설치 : 가장 처음에 봄버맨은 일부 칸에 폭탄을 설치해 놓는다. 모든 폭탄이 설치된 시간은 같다.
graph = [list(input().rstrip()) for _ in range(r)]

# 위치 이동
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()


def bfs(q, data):
    while q:
        x, y = q.popleft()
        # 폭탄 위치 폭발
        data[x][y] = '.'
        # 폭탄 위치와 인접한 상,하,좌,우 터트리기
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < r and 0 <= ny < c and data[nx][ny] == 'O':
                data[nx][ny] = '.'


def simulate(time):
    global graph, q
    # 1초 동안 봄버맨은 아무것도 하지 않는다 => 첫 1초에는 아무일도 X
    if time == 1:
        for i in range(r):
            for j in range(c):
                if graph[i][j] == 'O':
                    q.append((i, j))  # q에 첫 폭탄 위치 저장
    # 3초일때
    elif time % 2 == 1:
        # BFS = 폭탄 터트리기
        bfs(q, graph)
        # 안 터진 폭탄 위치 큐에 저장
        for x in range(r):
            for y in range(c):
                if graph[x][y] == 'O':
                    q.append((x, y))
    # 3초가 아닐때 => 모든 위치에 폭탄 설치
    else:
        graph = [['O']*c for _ in range(r)]


for i in range(1, n+1):
    simulate(i)

for row in graph:
    print(''.join(row))

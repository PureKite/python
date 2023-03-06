n = int(input())
num = int(input())

data = [[0] * n for _ in range(n)]  # 0으로 채워넣기

data[0][0] = n**2

# 아래, 왼쪽, 위, 오른쪽
# direction = ['D', 'L', 'U', 'R']
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0
d = 0
a, b = 1, 1  # 인덱스값 초기 설정
while True:
    nx = x + dx[d]
    ny = y + dy[d]

    # map을 벗어나는 경우, 이미 숫자가 들어간 경우 방향 바꾸기
    if nx < 0 or ny < 0 or nx >= n or ny >= n or data[nx][ny] > 0:
        d = (d+1) % 4
        continue

    data[nx][ny] = data[x][y]-1
    if data[nx][ny] == num:  # 정수 인덱스 찾기
        a, b = nx+1, ny + 1
    if data[nx][ny] == 1:  # 1일때 종료
        break
    x, y = nx, ny

for i in data:
    for j in i:
        print(j, end=' ')
    print()
print(a, b)

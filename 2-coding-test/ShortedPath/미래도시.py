INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())
# 2차원 리스트를 만들고, 모든 값을 무한으로 초기화
office = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            office[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for i in range(m):
    a, b = map(int, input().split())
    office[a][b] = 1
    office[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 k 입력받기
x, k = map(int, input().split())

# 점화식에 따라 폴로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            m1 = office[a][b]
            m2 = office[a][k]+office[k][b]
            office[a][b] = min(office[a][b], office[a][k]+office[k][b])

# 수행된 결과를 출력
distance = office[1][k] + office[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)

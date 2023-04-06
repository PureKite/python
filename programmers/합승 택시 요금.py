# 알고리즘은 알고 있었는데 응용력이 조금 부족했던 것 같다...
# 다익스트라랑 플로이드-워셜이랑 고민하다가
# 플로이드-워셜 알고리즘으로 풀다가 다익스트라 알고리즘 풀이를 보고
# 생각해낸 답안..
# => 응용력을 키워야겠다!
from heapq import heappop, heappush


def solution(n, s, a, b, fares):
    INF = int(1e9)
    taxi = [[INF] * (n+1) for _ in range(n+1)]

    for x in range(1, n+1):
        for y in range(1, n+1):
            if x == y:
                taxi[x][y] = 0
    for c, d, f in fares:
        taxi[c][d] = f
        taxi[d][c] = f
    for k in range(1, n+1):
        for x in range(1, n+1):
            for y in range(1, n+1):
                m1 = taxi[x][y]
                m2 = taxi[x][k]+taxi[k][y]
                taxi[x][y] = min(m1, m2)
    cost = taxi[s][a]+taxi[s][b]
    for i in range(1, n+1):
        if s != i:
            cost = min(cost, taxi[s][i]+taxi[i][a]+taxi[i][b])
    return cost


# 다익스트라로 푸는 방법 참고 : https://hbj0209.tistory.com/170
INF = int(1e9)
graph = [[]]


def preprocess(n, fares):
    global graph
    graph = [[] for i in range(n+1)]
    for fare in fares:
        src, dst, cost = fare[0], fare[1], fare[2]
        graph[src].append([dst, cost])
        graph[dst].append([src, cost])


def dijkstra(src, dst):
    global graph
    n = len(graph)
    table = [INF for i in range(n)]
    table[src] = 0
    pq = [[0, src]]
    while pq:
        w, x = heappop(pq)
        if table[x] < w:
            continue
        for item in graph[x]:
            nx, ncost = item[0], item[1]
            ncost += w
            if ncost < table[nx]:
                table[nx] = ncost
                heappush(pq, [ncost, nx])

    return table[dst]


def solution(n, s, a, b, fares):
    preprocess(n, fares)
    cost = dijkstra(s, a) + dijkstra(s, b)
    for i in range(1, n+1):
        if s != i:
            cost = min(cost, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    return cost

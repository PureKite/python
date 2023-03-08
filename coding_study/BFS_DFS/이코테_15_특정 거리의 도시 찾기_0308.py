# key word! '모든 도로의 거리는 1'이라는 조건! => 너비 우선 탐색 => 최단 거리 => bfs 활용

import sys
import heapq
from collections import deque
# 도시의 개수 n, 도로의 개수 m, 거리 정보 k, 출발 도시의 번호 x
# n, m, k, x = map(int, input().split()) # 입력 데이터 수가 많으므로 input() 대산 sys.stdin.readline() 사용 => 시간초과 X
n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # 단방향
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0  # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(bfs 수행)
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 k인 도시가 없다면, -1 출력
if check == False:
    print(-1)


# 다익스트라 최단 경로 알고리즘 활용

# f = sys.stdin.readline
# INF = int(1e9)

# n, m, k, x = map(int, f().split())
# graph = [[] for _ in range(n+1)]
# distance = [INF] * (n+1)

# for _ in range(m):
#     a, b = map(int, f().split())
#     graph[a].append((b, 1))  # 모든 도로의 길이 == 1을 같이 넣어줌


# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q: # bfs 풀이랑 비슷
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for j in graph[now]:
#             cost = dist + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
#                 heapq.heappush(q, (cost, j[0]))


# dijkstra(x)
# answer = []
# for i in range(1, n+1):
#     if distance[i] == k:
#         answer.append(i)

# if len(answer) == 0:
#     print(-1)
# else:
#     for i in answer:
#         print(i, end='\n')

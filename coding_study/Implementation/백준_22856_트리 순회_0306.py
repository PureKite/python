# import sys
# sys.setrecursionlimit(10**6)


# def input(): return sys.stdin.readline().rstrip()


# left = dict()
# right = dict()

# n = int(input())
# parent = [0] * (n+1)
# node_count = 0
# for _ in range(n):
#     a, b, c = map(int, input().split())
#     left[a] = b
#     right[a] = c

#     if b != -1:
#         parent[b] = a
#         node_count += 1
#     if c != -1:
#         parent[c] = a
#         node_count += 1

# last_node = 0


# def traverse(node):
#     global last_node
#     if node == -1:
#         return
#     traverse(left[node])
#     last_node = node
#     traverse(right[node])


# traverse(1)
# edge_count = node_count * 2
# movement = 0
# while last_node != 1:
#     movement += 1
#     last_node = parent[last_node]
# print(edge_count - movement)

# stack을 이용한 풀이
import sys
input = sys.stdin.readline

n = int(input())
right_nodes = [0]*(n+1)
for _ in range(n):
    data, _, r_node = map(int, input().split())
    right_nodes[data] = r_node

ans = 2*(n-1) + 1
stack = [1]
while stack:
    ans -= 1
    v = stack.pop()
    r_node = right_nodes[v]
    if r_node != -1:
        stack.append(r_node)
print(ans)

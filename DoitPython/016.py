import sys

input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    data.append((int(input()), i))

s_data = sorted(data)

max_value = 0
for i in range(n):
    if max_value < s_data[i][1] - i:
        max_value = s_data[i][1] - i

print(max_value + 1)


# 버블 정렬에서 안쪽 for문이 몇 번 수행됐는지 구하는 아이디어가 중요한 문제
# 데이터마다 정렬 전 index 값에서 정렬 후 index 값을 빼고 최댓값 찾기
# swap이 일어나지 않는 반복문이 한 번 더 실행되기 때문에 + 1

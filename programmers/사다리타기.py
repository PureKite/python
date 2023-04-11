# 시간초과..코드..
# product 함수를 사용해서 모든 경우를 넣기보다는 비교하는 방향이 더 빠르다!
# ?의 자리가 고정인 줄 알았는데 고정이 아니었음..

# import copy
# import sys
# from itertools import product
# input = sys.stdin.readline
# k = int(input())
# n = int(input())
# answer = list(input().rstrip())
# first = sorted(answer)
# data = [list(input()) for _ in range(n)]
# s = ['*', '-']

# for i in range(n):
#     for j in range(k-1):
#         if data[i][j] == '-':
#             first[j], first[j+1] = first[j+1], first[j]

# for i in product(s, repeat=k-1):
#     temp = copy.deepcopy(first)
#     for j in range(k-1):
#         if i[j] == '-':
#             temp[j], temp[j+1] = temp[j+1], temp[j]
#     for y in range(k-1):
#         if data[n-2][y] == '-':
#             temp[y], temp[y+1] = temp[y+1], temp[y]
#     for y in range(k-1):
#         if data[n-1][y] == '-':
#             temp[y], temp[y+1] = temp[y+1], temp[y]
#     if temp == answer:
#         print(''.join(map(str, i)))
#         sys.exit(0)

# print('x'*(k-1))

# 참고 : https://velog.io/@highero-k/%EB%B0%B1%EC%A4%80-2469-%EC%82%AC%EB%8B%A4%EB%A6%AC-%ED%83%80%EA%B8%B0-Python-%EA%B3%A8%EB%93%9C-5
# 1. ?를 기준으로 사다리 나누기
# 2. ? 앞에 사다리 타기
# 3. ? 뒤에 사다리 타기
# 3. 앞 뒤 값 비교하기

k = int(input())
n = int(input())
end = list(input())
start = sorted(end)
data = [list(input()) for _ in range(n)]
data_s = []
data_e = []

for i in range(len(data)):
    if data[i][0] == '?':
        data_s = data[:i]
        data_e = data[i+1:]
        break

for i in data_s:
    for j in range(k-1):
        if i[j] == '-':
            start[j], start[j+1] = start[j+1], start[j]

data_e.reverse()
for i in data_e:
    for j in range(k-1):
        if i[j] == '-':
            end[j], end[j+1] = end[j+1], end[j]
answer = []
for i in range(len(start)-1):
    if start[i] == end[i]:
        answer.append("*")
    else:
        if start[i] == end[i+1]:
            answer.append('-')
        elif i != 0 and start[i] == end[i-1]:
            answer.append('*')
        else:
            answer = ['x' for _ in range(k-1)]
            break
print(''.join(answer))

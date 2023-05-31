# import sys

# input = sys.stdin.readline

# n = int(input())
# data = []
# temp = []
# result = []
# sol = []
# for _ in range(n):
#     data.append(int(input()))
# while data:
#     top = data[-1]
#     if not temp:
#         sol.append("-")
#         temp.append(top)
#         data.pop()
#     elif temp[-1] < top:
#         sol.append("-")
#         temp.append(top)
#         data.pop()
#     else:
#         sol.append("+")
#         result.append(temp.pop())
# for i in range(len(temp)):
#     sol.append("+")
# result.reverse()
# temp.extend(result)
# if list(range(1, n + 1)) == temp:
#     for i in range(len(sol) - 1, -1, -1):
#         print(sol[i])
# else:
#     print("NO")

# # 책에서 정의한 풀이
# n = int(input())
# data = [0] * n

# for i in range(n):
#     data[i] = int(input())

# stack = []
# num = 1
# result = True
# answer = ""

# for i in range(n):
#     su = data[i]
#     if su >= num:
#         while su >= num:
#             stack.append(num)
#             num += 1
#             answer += "+\n"
#         stack.pop()
#         answer += "-\n"
#     else:
#         n = stack.pop()
#         if n > su:
#             print("NO")
#             result = False
#             break
#         else:
#             answer += "-\n"

# if result:
#     print(answer)


# 시간이 빠른 풀이
# 참고 : https://www.acmicpc.net/source/58324396
import sys


def solution():
    # *nums 이렇게 표현할 수 있다는 것을 배웠다..!
    n, *nums = map(int, sys.stdin.buffer.read().splitlines())
    s = []
    answer = []
    cur = 1
    for value in nums:
        while cur <= value:
            answer.append("+")
            s.append(cur)
            cur += 1
        if s.pop() != value:
            return "NO"
        answer.append("-")
    return "\n".join(answer)


print(solution())

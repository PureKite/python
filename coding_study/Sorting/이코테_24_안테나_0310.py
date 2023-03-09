import sys
input = sys.stdin.readline
n = int(input())
antenna = list(map(int, input().split()))

antenna.sort()
print(antenna[(n-1)//2])
# if len(antenna) % 2 == 0:
#     print(antenna[len(antenna)//2 - 1])
# else:
#     print(antenna[(n-1)//2])

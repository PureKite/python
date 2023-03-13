import sys


def binary_search(array, target, start, end):
    mid = (end + start) // 2
    if start > end:
        return print('no', end=' ')
    elif array[mid] == target:
        return print('yes', end=' ')
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)


input = sys.stdin.readline
n = int(input())
n_data = list(map(int, input().split()))
n_data.sort()
m = input()
m_data = list(map(int, input().split()))


for i in m_data:
    binary_search(n_data, i, 0, n-1)


# 예시 답안
def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


# 계수 정렬
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))
for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 집합 자료형 이용
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 시간 복잡도를 고려해야함..
# list의 길이가 최대 백만이므로.... 최악의 경우 1+2+....100만 = 100만*100만/2 = 5천억번의 연산이 필요합니다.
# index 말고 다른 방법을 찾는 것이 중요..!
import sys
input = sys.stdin.readline
n = int(input())
x = list(map(int, input().split()))
# 중복 없애줌
data = list(set(x))
data.sort()
# list.index(i)의 형태는 시간복잡도 O(N)을 가지고 있고 그렇다면 매번 최대 1,000,000번의 수행이 이루어지게 돼서
# 시간초과가 나는 것 => 때문에 이를 해결하기 위해 dict 사용
# list.index(i) 형태의 시간 복잡도 = O(N), index[i] 형태의 시간 복잡도 = O(1)
dict = {data[i]: i for i in range(len(data))}
for i in x:
    print(dict[i], end=' ')

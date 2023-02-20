# 집합의 핵심 : 원소가 고유하다.(중복 X), 순서가 없다.

s1 = set([1, 2, 3])
print(s1)
s1 = {1,2,3}
print(s1)
l = [1,2,2,3,3]
newl = list(set(l))
print(newl)
s1 = set("Hello")
print(s1)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

## 집합 자료형 관련 함수들
s1 = set([1, 2, 3])

# 값 1개 추가하기 add
s1.add(4)
print(s1)

# 값 여러 개 추가하기 update
s1.update([4,5,6])
print(s1)

# 특정 값 제거하기 remove
s1.remove(2)
print(s1)
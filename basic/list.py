a = [1, 2, 3, 4, 5] # 리스트

a[4] # 인덱스 4, 다섯 번째 원소에 접근

b = list() # 빈 리스트 선언 방법 1
c = [] # 빈 리스트 선언 방법 2

# 리스트 안에 리스트 넣기 가능
a = [1, 2, ['a', 'b']]
print(a[2][0])
print(a)
a[2] = 3
print(a)

# del 함수 사용해 리스트 요소 삭제하기
a = [1,2,3]
del a[1]
print(a)

# 리스트 길이구하기
a = [1, 2, 3]
print(len(a))

## 관련 함수들
# 리스트에 요소 추가 append
a = [1, 2, 3]
a.append(4)
print(a)

# 리스트 정렬 sort
a = [1, 4, 3, 2]
a.sort()
print(a) 

# 리스트 뒤집기 reverse
a = [1, 4, 3, 2]
a.reverse()
print(a) 

# 인덱스 반환 index
a = [1, 2, 3]
print(a.index(3)) # 리스트에 존재하지 않으면 값 오류 발생

# 리스트에 요소 삽입 insert(a, b) a 번째 위치에 b 삽입
a = [1, 5, 3]
a.insert(0, 4)
print(a)

# 리스트 요소 제거 remove
a = [1, 2, 3, 1, 2, 3] 
a.remove(3) # 첫 번째로 나오는 3 삭제
print(a)

# 리스트 요소 끄집어내기 pop
a = [1, 2, 3]
print(a.pop())
print(a)

# 리스트에 포함된 요소 x의 개수 세기(count)
a = [1, 2, 3, 1]
print(a.count(1))

# 리스트 확장 extend  == a += [4, 5]
a.extend([4, 5])
print(a)
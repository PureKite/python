# 변수를 만들 때는 =를 사용
a = 1
b = 'python'

# 파이썬에서 사용하는 변수는 객체를 가리키는 것
# Python Tutor 참고

a = [1, 2, 3]
b = a # a의 주소를 b에 넣음. 즉, a와 b는 완전 동일
a[1] = 4
print(a)
print(b)
print(a is b)
print(id(a))
print(id(b))

## 복사할려면?
# [:] 이용
a = [1, 2, 3]
b = a[:]
print(a)
print(b)
print(a is b)
print(id(a))
print(id(b))

# copy 모듈 이용
from copy import copy
a = [1, 2, 3]
b = copy(a)
print(a)
print(b)
print(a is b)
print(id(a))
print(id(b))

# 변수를 만드는 여러 가지 방법
a, b = ('python', 'life')
print(a)
print(b)
(a, b) = 'python', 'life'
print(a)
print(b)
[a,b] = ['python', 'life']
print(a)
print(b)
a = b = 'python'
print(a)
print(b)
a = 3
b = 5
a, b = b, a
print(a)
print(b)
# 문자 개수 세기 count
a = "hobby"
print(a.count('b'))

# 위치 알려주기 find
a = "hobby"
print(a.find('b')) # 없으면 -1

# 위치 알려주기 index
a = "hobby"
print(a.index('b')) # 없으면 에러

# 문자열 삽입 join
a = ","
print(a.join('abcd'))

# 소문자를 대문자로 바꾸기 upper
a = "hi"
print(a.upper())

# 대문자를 소문자로 바꾸기 lower
a = "HI"
print(a.lower())

# 공백 지우기 strip
a = " hi "
print(a.strip()) # 왼쪽 공백 지우기 - lstrip, 오른쪽 공백 지우기 - rstrip

# 문자열 바꾸기 replace
a = "Life is too short"
print(a.replace('Life', 'Your leg'))

# 문자열 나누기 split
a = "Life is too short"
print(a.split())
b = "a:b:c:d"
print(b.split(':'))
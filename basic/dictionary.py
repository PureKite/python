# 루비 - Hash, 자바 - Map, 자바스크립트 - Object, JSON 형식
# API에 자주 활용됨, 연관 배열 또는 해시

# 딕셔너리 {Key1:Value1, Key2:Value2, Key3:Value3, ...}
dic = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print(dic['name'])

a = {1: 'a'}
a['name'] = '익명'
print(a)

del a[1] # key 입력
print(a)

# 딕셔너리 만들 때 주의할 사항
a = {1: 'a', 1: 'b'} # key 중복 불가능
print(a)

## 딕셔너리 관련 함수들
# Key 리스트 만들기 keys
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())
print(a.values())
print(a.items())
for k in a.keys():  #values(), items() 등등
    print(k)

# Key: Value 쌍 모두 지우기 clear
a.clear()
print(a)

# Key로 Value 얻기 get
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('name'))
print(a.get(1)) # 없는 값이면 에러가 아니라 None 출력
print(a.get(1, '없음')) # None 대신 다른 글자로 변경 가능

# 해당 Key가 딕셔너리 안에 있는지 조사하기 in
print('phone' in a) # True/False
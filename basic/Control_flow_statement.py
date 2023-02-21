# if문
money = True
if money:
    print("택시")
else:
    print("걷기")

## 비교 연산자
# x < y : x가 y보다 작다.
# x > y : x가 y보다 크다.
# x == y : x와 y가 같다.
# x != y : x와 y가 같지 않다.
# x >= y : x가 y보다 크거나 같다.
# x <= y : x가 y보다 작거나 같다.

## and, or, not
# x or y : x와 y 둘중에 하나만 참이어도 참이다. |
# x and y : x와 y 모두 참이어야 참이다. &
# not x : x가 거짓이면 참이다. !

## in, not in : ~ 안에
# x in 리스트 / x not in 리스트
# x in 튜플 / x not in 튜플
# x in 문자열 / x not in 튜플

if 1 in [1,2,3]:
    print(',')

## 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
# pass : 통과

# 조건이 여러개라면?
# elif 사용
pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print('택시')
elif card:
    print('택시')
else:
    print('걷기')

# 조건부 표현식 / 3항 연산자 ?의 파이썬 버전
score = 70
message = 'success' if score >= 60 else "failure"
print(message)

# while문
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.") 
    # break : 반복문 빠져나가기

# continue : while문의 맨 처음으로 돌아가기
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

# 무한 루프
# while True: 
#     수행할 문장1 
#     수행할 문장2
#     ...


# for 문
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2
#     ...

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

# for문과 continue
marks = [90, 25, 67, 45, 80]
number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60: continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)

# for문과 함께 자주 사용하는 range 함수
add = 0
for i in range(1, 11):
    add = add + i
    print(add)

# for와 range를 이용한 구구단
for i in range(2,10):        # 1번 for문
    for j in range(1, 10):   # 2번 for문
        print(i*j, end=" ") 
    print('')

# 리스트 내포, 리스트 컴프리헨션 [표현식 for 항목 in 반복가능객체 if 조건문]
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]

result = []
for num in a:
    if num % 2 == 0:
        result.append(num * 3)
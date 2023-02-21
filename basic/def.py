# 함수
# - 입력(input)값을 가지고 어떤 일을 수행한 다음에 출력(output)값을 내놓는 것 / but, 입력, 출력 없을 수 있음

# 함수를 사용하는 이유?
# - 반복되는 부분이 있을 경우 편하다.
# - 기능 단위의 함수로 분리해 놓으면 프로그램 흐름을 일목요연하게 볼 수 있기 때문

# 파이썬 함수의 구조
# def 함수명(매개변수):
#     <수행할 문장1>
#     <수행할 문장2>

def sum(a, b):
    result = a + b
    return result

# 호출
print(sum(1,2))

# 입력/출력이 없는 경우
def say():
    print('Hi')
say()
print(say()) # 출력값이 없는 경우 : None

# 입력값이 몇 개가 될지 모를 때
def sum_many(*args): # 관습 args
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(sum_many(1,2,3))

# 키워드 매개변수 딕셔너리 형태
def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if k == 'name':
            print("당신의 이름은 : " + kwargs[k])
print_kwargs(name='int 조수', b = '2')

# 함수의 리턴값은 언제나 하나
def sum_and_mul(a, b):
    return a+b, a*b
print(sum_and_mul(1,2)) # 튜플 형식
print(sum_and_mul(1,2)[0]) # 하나의 값만 사용하고 싶다면

# 초기값 미리 설정
def say_myself(name, age, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")

say_myself("라이유튜브", 20)
say_myself("라이유튜브", 20, False) # 함수 위치는 맞춰야함. 변수 매핑한다면 괜찮.

# 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a): # 지역변수, 범위는 함수까지
    a = a + 1

vartest(a)
print(a) ## 값의 변동은 자료형에 따라 변동될 수 있음(Mutable)

## 영향을 줄려면?
a =  1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

a = 1
def vartest():
    global a
    a = a+1
vartest()
print(a)

# lambda
add = lambda a, b : a+b
print(add(1,2))
myList = [lambda a, b : a+b, lambda a, b : a*b]
print(myList[0](1,2))
print(myList[1](1,2))
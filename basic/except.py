try:
    # 오류가 발생할 수 있는 구문
    pass
except Exception as e:
    # 오류 발생
    pass
else:
    # 오류 발생하지 않음
    pass
finally:
    # 무조건 마지막에 실행
    pass

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

print('hi')

try:
    f = open('none', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    print(data)
    f.close()

# f = open('foo.txt', 'w')
# try:
#     data = f.read()
#     print(data)
# except Exception as e:
#     print(e)
# finally:
#     f.close()

# 오류 회피하기
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass

# 오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError # NotImplementedError는 파이썬에 이미 정의되어 있는 오류로, 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류를 일으키기 위해 사용
    
class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()

# 예외 만들기
class MyError(Exception):
    pass
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")